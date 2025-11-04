from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import DonorRegistrationForm, DonorLoginForm
from .models import Donor

def register_view(request):
    if request.method == 'POST':
        form = DonorRegistrationForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.set_password(form.cleaned_data['password'])
            donor.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = DonorRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = DonorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = DonorLoginForm()
    return render(request, 'users/login.html', {'form': form})

def home_view(request):
    return render(request, 'users/home.html')
