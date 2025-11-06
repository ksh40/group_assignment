from django.shortcuts import render
from django.contrib import messages
from .forms import DonationForm


def donations_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.save()
            messages.success(request, 'Donation made')
    else:
        form = DonationForm()
        messages.error(request, 'Donation not made: Invalid funds')
    return render(request, 'donations/donate.html', {'form': form})

def home_view(request):
    return render(request, 'users/home.html')
