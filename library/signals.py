from django.dispatch import receiver
from allauth.account.signals import user_logged_in
from .models import Profile

@receiver(user_logged_in)
def set_user_role(sender, request, user, **kwargs):
    # Check if the user logged in via Google
    if user.socialaccount_set.filter(provider='google').exists():
        profile, created = Profile.objects.get_or_create(user=user)
        # Only set the role if it hasn't been assigned yet
        if not profile.role:
            profile.role = 'patron'
            profile.save() 