# parking_finder/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('parking.urls')),  # Include URLs from the parking app
]