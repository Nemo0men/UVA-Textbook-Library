from .models import Notification

def notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            user=request.user
        ).order_by('-created_at')[:5]
        return {'notifications': notifications}
    return {'notifications': []}

def theme(request):
    if request.user.is_authenticated:
        theme = request.user.profile.preference
    else:
        theme = request.session.get('theme', 'light')
    return {'theme': theme} 