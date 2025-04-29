from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Book, ApprovedLibrarianEmail, Profile, Collection

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(ApprovedLibrarianEmail)
class ApprovedLibrarianEmailAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'profile_picture')
    search_fields = ('user__username', 'user__email')
    list_filter = ('role',)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user')
    search_fields = ('title', 'user__username')
    list_filter = ('user',)

# Define an inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin) 