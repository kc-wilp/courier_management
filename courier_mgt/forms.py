from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Bookings , Profile


class BookingForm(forms.ModelForm):
    # your_name = forms.CharField(label='Your name', max_length=100)

    class Meta:

        model = Bookings
        fields = ['booking_id', 'booking_name', 'booking_email' ]


class UserForm(UserCreationForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
