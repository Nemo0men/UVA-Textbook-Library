from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore_library, name='explore_library'),
    path('my-library/', views.my_library, name='my_library'),
    path('librarian/', views.librarian_dashboard, name='librarian_dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('redirect/', views.assign_role, name='redirect'),
    path('profile/', views.profile, name='profile'),
    path('collections/', views.collections, name='collections'),
    path('collections/<int:collection_id>/', views.collection_detail, name='collection_detail'),
    path('change-password/', 
        login_required(auth_views.PasswordChangeView.as_view(
            template_name='library/change_password.html',
            success_url='/library/change-password-done/'
        )), 
        name='change_password'),
    path('change-password-done/', 
        login_required(auth_views.PasswordChangeDoneView.as_view(
            template_name='library/change_password_done.html'
        )),
        name='password_change_done'),
    path('add-to-collection/<int:book_id>/', views.add_to_collection, name='add_to_collection'),
    path('collections/<int:collection_id>/remove/<int:book_id>/', views.remove_from_collection, name='remove_from_collection'),
    path('book/<int:book_id>/pdf/', views.view_pdf, name='view_pdf'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/rent/', views.rent_book, name='rent_book'),
    path('collections/<int:collection_id>/delete/', views.delete_collection, name='delete_collection'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('approve-rentals/', views.approve_rentals, name='approve_rentals'),
    path('my-pending-rentals/', views.my_pending_rentals, name='my_pending_rentals'),
] 