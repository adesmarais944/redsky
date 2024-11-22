from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Chirp

def home(request):
    if request.user.is_authenticated:
        chirps = Chirp.objects.all().order_by("-created_at")
    return render(request, 'home.html', {"chirps":chirps})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ('You must be logged in to view this page.'))
        return redirect('home')
    
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        chirps = Chirp.objects.filter(user_id=pk).order_by("-created_at")
        # POST form logic
        if request.method == "POST":
            # Get current user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)
            current_user_profile.save()

        return render(request, 'profile.html', {"profile":profile, "chirps":chirps})
    else:
        messages.success(request, ('You must be logged in to view this page.'))
        return redirect('home')