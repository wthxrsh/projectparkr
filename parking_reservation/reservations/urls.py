from django.urls import path
from .views import home, signup, post_parking_space, view_parking_spaces, book_parking_space, login_view, logout_view, my_bookings, delete_parking_space, delete_booking

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('post_parking_space/', post_parking_space, name='post_parking_space'),
    path('view_parking_spaces/<str:city>/', view_parking_spaces, name='view_parking_spaces'),
    path('book_parking_space/<int:space_id>/', book_parking_space, name='book_parking_space'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('my_bookings/', my_bookings, name='my_bookings'),
    path('delete_parking_space/<int:space_id>/', delete_parking_space, name='delete_parking_space'),
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),  # Add this line
]