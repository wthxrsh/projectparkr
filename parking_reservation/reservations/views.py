import qrcode
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ParkingSpaceForm
from .models import ParkingSpace, Booking
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ParkingSpaceForm
from .models import ParkingSpace
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ParkingSpace
from .forms import ParkingSpaceForm

@login_required
def post_parking_space(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        location = request.POST.get('location')
        price_per_hour = request.POST.get('price_per_hour')

        # Create a new ParkingSpace instance
        parking_space = ParkingSpace(
            city=city,
            location=location,
            price_per_hour=price_per_hour,
            owner=request.user  # Set the owner to the currently logged-in user
        )
        parking_space.save()  # Save the instance to the database
        return redirect('view_parking_spaces', city=city)  # Redirect to the city's parking space list
    else:
        form = ParkingSpaceForm()
    return render(request, 'post_parking_space.html', {'form': form})

@login_required
def view_parking_spaces(request, city):
    parking_spaces = ParkingSpace.objects.filter(city=city)  # Filter by city
    return render(request, 'view_parking_spaces.html', {'parking_spaces': parking_spaces, 'city': city})

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)  # Get bookings for the logged-in user
    return render(request, 'my_bookings.html', {'bookings': bookings})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            # Check if "remember me" is checked
            remember_me = request.POST.get('remember_me')
            if remember_me:
                # Set the session to expire in 30 days
                request.session.set_expiry(60 * 60 * 24 * 30)  # 30 days
            else:
                # Default session expiry (browser close)
                request.session.set_expiry(0)  # Session expires when the browser is closed

            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def book_parking_space(request, space_id):
    parking_space = ParkingSpace.objects.get(id=space_id)
    if request.method == 'POST':
        hours = request.POST.get('hours')
        qr_code = f"Booking-{request.user.id}-{parking_space.id}-{hours}"
        img = qrcode.make(qr_code)
        img.save(f'media/qr_codes/{qr_code}.png')
        booking = Booking.objects.create(parking_space=parking_space, user=request.user, hours=hours, qr_code=qr_code)
        return render(request, 'booking_success.html', {'qr_code': qr_code})
    return render(request, 'book_parking_space.html', {'parking_space': parking_space})
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ParkingSpace

@login_required
def delete_parking_space(request, space_id):
    parking_space = get_object_or_404(ParkingSpace, id=space_id, owner=request.user)
    if request.method == 'POST':
        parking_space.delete()
        return redirect('view_parking_spaces', city=parking_space.city)  # Redirect to the city view
    return render(request, 'confirm_delete.html', {'parking_space': parking_space})

from django.shortcuts import render, get_object_or_404
from .models import Booking  # Assuming you have a Booking model

def booking_successful(request, booking_id):
    # Fetch the booking object based on the booking_id
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_success.html', {'booking': booking})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking  # Assuming you have a Booking model

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)  # Ensure the user is the owner
    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')  # Redirect back to the My Bookings page
    return render(request, 'confirm_delete_booking.html', {'booking': booking})