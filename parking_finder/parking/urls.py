from django.urls import path
from .views import (
    home_view,
    find_spots,
    post_spot,
    book_spot,
)

urlpatterns = [
    path('', home_view, name='home'),  # Home page
    path('find_spots/', find_spots, name='find_spots'),  # Find parking spots
    path('post_spot/', post_spot, name='post_spot'),  # Post a new parking spot
    path('book_spot/<int:spot_id>/', book_spot, name='book_spot'),  # Book a parking spot
]