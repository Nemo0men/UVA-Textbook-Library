from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

class Book(models.Model):
    CONDITION_CHOICES = (
        ('new', 'New'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    )
    
    # Add ISBN as primary identifier
    isbn = models.CharField(max_length=13, unique=True, help_text="13-digit ISBN")
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, help_text="Book description")
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='book_pdfs/', blank=True, null=True)
    rental_price = models.DecimalField(max_digits=6, decimal_places=2, default=9.99)
    rental_duration_days = models.IntegerField(default=30)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='good')
    
    @property
    def average_rating(self):
        ratings = self.bookrating_set.all()
        if not ratings:
            return 0
        return sum(r.rating for r in ratings) / len(ratings)

    def __str__(self):
        return f"{self.title} (ISBN: {self.isbn})"

class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Library"

class Profile(models.Model):
    USER_ROLES = (
        ('librarian', 'Librarian'),
        ('patron', 'Patron'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='patron')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class ApprovedLibrarianEmail(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email 
    

class Collection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    books = models.ManyToManyField(Book, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='collection_covers/', blank=True, null=True)
    is_private = models.BooleanField(default=False)
    allowed_users = models.ManyToManyField(User, blank=True, related_name='accessible_collections')
    access_requests = models.ManyToManyField(User, blank=True, related_name='requested_collections')

    def clean(self):
        if not hasattr(self, 'user'):
            return
            
        if self.is_private and not self.user.profile.role == 'librarian':
            raise ValidationError({
                'is_private': "Only librarians can create private collections."
            })

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def can_add_items(self, user):
        """Check if a user can add items to this collection"""
        if self.user == user:  # Collection owner can always add items
            return True
        if user.profile.role == 'librarian':  # Librarians can add to any collection
            return True
        if self.user.profile.role == 'librarian':  # Patrons can't add to librarian collections
            return False
        return True  # Patrons can add to other patron collections

class Rental(models.Model):
    RENTAL_STATUS = (
        ('pending_approval', 'Pending Librarian Approval'),
        ('pending', 'Pending Payment'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=RENTAL_STATUS, default='pending')
    payment_id = models.CharField(max_length=100, blank=True, null=True)

    def days_remaining(self):
        if not self.end_date:
            return 0
        now = timezone.now()
        if isinstance(self.end_date, str):
            end_date = timezone.datetime.fromisoformat(self.end_date)
        else:
            end_date = self.end_date
        remaining = (end_date - now).total_seconds() / 60  # Convert to minutes
        return max(0, int(remaining))

    def is_active(self):
        return self.status == 'active' and self.days_remaining() > 0

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"

class FakeInvoice(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=6)
    issued_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.message[:50]}"

class BookRating(models.Model):
    RATING_CHOICES = (
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent')
    )
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('book', 'user')  # One rating per user per book

    def __str__(self):
        return f"{self.user.username}'s rating for {self.book.title}"