import io

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, PasswordChange
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, "profile.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been successfully logged in.')
            return redirect('home')
        else:
            messages.success(request, 'Error in logging in! Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            object = form.save(commit=False)
            object.email = object.username
            object.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered.")
            if user.is_authenticated:
                return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully edited your profile.")
            return redirect('home_menu')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'profile.html', context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChange(data=request.POST or None, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully changed your password.")
            return redirect('home')
    else:
        form = PasswordChange(user=request.user)
    context = {'form': form}
    return render(request, 'password.html', context)