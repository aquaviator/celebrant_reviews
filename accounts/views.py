from django.shortcuts import render, redirect, get_object_or_404
from .forms import CelebrantRegisterForm, ReviewForm  # Import both the registration and review forms
from django.urls import reverse  # Import reverse to use named URL
from django.contrib.auth.models import User  # Import User model for celebrants

# Home page view
def home(request):
    return render(request, 'home.html')  # Render the home page template

# Registration view
def register(request):
    if request.method == 'POST':
        form = CelebrantRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CelebrantRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

# Review submission view
def submit_review(request, celebrant_id):
    celebrant = get_object_or_404(User, id=celebrant_id)  # Get the celebrant by their ID
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.celebrant = celebrant  # Link the review to the celebrant
            review.save()
            return redirect('home')  # Redirect after successful submission
    else:
        form = ReviewForm()

    return render(request, 'accounts/submit_review.html', {'form': form, 'celebrant': celebrant})
