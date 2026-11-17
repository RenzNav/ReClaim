from django.shortcuts import render
from .models import Listing
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ListingForm


def home(request):
    listings = Listing.objects.filter(is_available=True)

    return render(request, 'core/home.html', {
        'listings': listings
    })


def browse(request):
    return render(request, 'core/browse.html')


@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.donor = request.user
            listing.save()

            return redirect('home')
    else:
        form = ListingForm()

    return render(request, 'core/create_listing.html', {
        'form': form
    })


def requests(request):
    return render(request, 'core/requests.html')