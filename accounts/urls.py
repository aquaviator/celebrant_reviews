from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import for login view

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration URL
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  # Login URL
    path('celebrant/<int:celebrant_id>/review/', views.submit_review, name='submit_review'),  # Add review submission URL
]
