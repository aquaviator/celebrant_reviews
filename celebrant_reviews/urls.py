from django.contrib import admin
from django.urls import path, include
from accounts.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include the accounts app URLs
    path('', home, name='home'),  # Root URL for the home page
]
