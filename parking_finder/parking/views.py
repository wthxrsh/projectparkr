from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, ParkingSpot
from django.contrib import messages

# Home view
def home_view(request):
    return render(request, 'parking/home.html')  # Render the home page

# View for finding parking spots
def find_spots(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        spots = ParkingSpot.objects.filter(city=city)  # Filter spots by selected city
        return render(request, 'parking/spots.html', {'spots': spots, 'city': city})
    return redirect('home')  # Redirect to home if not a POST request

# View to post a new parking spot
def post_spot(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        price = request.POST.get('price')
        description = request.POST.get('description')
        ParkingSpot.objects.create(city=city, price=price, description=description)  # Create a new parking spot
        return redirect('home')  # Redirect to home after posting
    return render(request, 'parking/post_spot.html')  # Render the post spot form

# View to book a parking spot
def book_spot(request, spot_id):
    spot = get_object_or_404(ParkingSpot, id=spot_id)  # Get the parking spot by ID
    if request.method == 'POST':
        hours = int(request.POST.get('hours'))
        total_price = spot.price * hours
        booking = Booking(parking_spot=spot, hours=hours, total_price=total_price)
        booking.save()  # Save the booking
        
        # Add a success message
        messages.success(request, 'Booked successfully!')
        return redirect('home')  # Redirect to the home page
    return render(request, 'parking/book_spot.html', {'spot': spot})  # Render the booking form