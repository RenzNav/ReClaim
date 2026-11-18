from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Listing
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ListingForm
from django.contrib.auth import login
from .forms import RegisterForm


def home(request):
    # Display all available listings on the home page
    listings = Listing.objects.filter(is_available=True)

    return render(request, 'core/home.html', {
        'listings': listings
    })


def browse(request):
    return render(request, 'core/browse.html')


@login_required
def create_listing(request):
    # Handle submitted listing information
    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.donor = request.user
            listing.save()

            return redirect('home')
    else:
        # Display an empty listing form
        form = ListingForm()

    return render(request, 'core/create_listing.html', {
        'form': form
    })


def requests(request):
    return render(request, 'core/requests.html')


def register(request):
    # Handle submitted registration information
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # Create the new user account
            user = form.save()

            # Automatically log in the newly registered user
            login(request, user)

            return redirect('home')

    else:
        # Display an empty registration form
        form = RegisterForm()

    return render(request, 'core/register.html', {
        'form': form
    })


@login_required
def my_listings(request):
    # Retrieve only listings created by the logged-in user
    listings = Listing.objects.filter(
        donor=request.user
    ).order_by('-created_at')

    return render(request, 'core/my_listings.html', {
        'listings': listings
    })


@login_required
def edit_listing(request, listing_id):
    # Find the listing, ensuring it belongs to the logged-in user
    listing = get_object_or_404(
        Listing,
        id=listing_id,
        donor=request.user
    )

    if request.method == 'POST':
        # Populate the form with the submitted changes
        form = ListingForm(request.POST, instance=listing)

        if form.is_valid():
            # Update the existing listing
            form.save()
            return redirect('my_listings')
    else:
        # Display the form with the listing's current information
        form = ListingForm(instance=listing)

    return render(request, 'core/edit_listing.html', {
        'form': form,
        'listing': listing
    })


@login_required
def delete_listing(request, listing_id):
    # Find the listing and verify ownership
    listing = get_object_or_404(
        Listing,
        id=listing_id,
        donor=request.user
    )

    # Only delete the listing after form submission
    if request.method == 'POST':
        listing.delete()
        return redirect('my_listings')

    return render(request, 'core/delete_listing.html', {
        'listing': listing
    })
