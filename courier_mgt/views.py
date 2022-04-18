import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.http import HttpResponseRedirect

from .forms import BookingForm, UserForm, ProfileUpdateForm , UserUpdateForm

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from .models import Bookings


# Create your views here.


customers = [

{
    'customer_id': 1,
    'customer_name': "Kaushik",
    'customer_email': 'kaushik@email.com'

},
{
    'customer_id': 2,
    'customer_name': "Ram",
    'customer_email': 'ram@email.com'

}

]



def register(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}, your account has been created! Please login')
            return redirect('login')

    else:
        form = UserForm()

    return render(request, 'courier_mgt/register.html', {'form': form})
    
@login_required
def profile(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated! Please login')
            return redirect('site-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'courier_mgt/profile.html', context)



@login_required
def home(request):

    context = {
        'customers': customers
    }

    return render(request, 'courier_mgt/index.html', context)


##### CRUD OPERATION - create retrieve update and delete

# retrieve/ list all bookings
@login_required
def booking_list(request):

    bookings = Bookings.objects.all()

    print(bookings)


    context = {
        'bookings': bookings
    }

    return render(request, 'courier_mgt/index.html', context)



# detail/ retrieve a specific booking
@login_required
def booking_detail(request, id):

    booking = Bookings.objects.get(id=id)

    print(booking)


    context = {
        'booking': booking
    }

    return render(request, 'courier_mgt/detail.html', context)

# create/ create a specific booking
@login_required
def booking_create(request):

    form = BookingForm(request.POST or None)

    if form.is_valid():

        print(form.cleaned_data)
        id = form.cleaned_data['booking_id']
        name = form.cleaned_data['booking_name']
        email = form.cleaned_data['booking_email']
        
        new_booking = Bookings.objects.create(booking_id = id, booking_name = name, booking_email = email )

        return redirect('/')



    context = {
        'form': form
    }

    return render(request, 'courier_mgt/create.html', {'form': form})

# create/ create a specific booking
@login_required
def booking_update(request, id):

    booking = Bookings.objects.get(id = id)
    form = BookingForm(request.POST or None, instance= booking )

    if form.is_valid():

        print(form.cleaned_data)
        form.save()
        # id = form.cleaned_data['booking_id']
        # name = form.cleaned_data['booking_name']
        # email = form.cleaned_data['booking_email']
        
        # new_booking = Bookings.objects.create(booking_id = id, booking_name = name, booking_email = email )

        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'courier_mgt/update.html', {'form': form})

@login_required
def booking_delete(request, id):

    booking = Bookings.objects.get(id = id)
    booking.delete()

    return redirect('/')

    