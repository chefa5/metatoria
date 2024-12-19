from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as leave
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import ProfileChangeForm, UserLoginForm, UserRegistrationForm
from users.models import User



def auth(request):

    login_form = UserLoginForm()
    registration_form = UserRegistrationForm()

    if request.method == 'POST':
        print(request.POST)
        if 'login' in request.POST:
            print('log')
            login_form = UserLoginForm(data=request.POST)
            if login_form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse('users:profile'))
                
        elif 'password1' in request.POST:
            registration_form = UserRegistrationForm(data=request.POST)
            if registration_form.is_valid():
                registration_form.save()
                return HttpResponseRedirect(reverse('users:auth'))
    else:
        login_form = UserLoginForm()
        registration_form = UserRegistrationForm()
    context = {
        'login_form': login_form,
        'registration_form': registration_form,
    }
    return render(request, 'users/auth.html', context)

@login_required
def profile(request):
    user_info = request.user
    if request.method == 'POST':
        change_form = ProfileChangeForm(data=request.POST, instance=request.user, files=request.FILES)
        if change_form.is_valid():
            change_form.save()
            return HttpResponseRedirect(request.path)
    else:
        change_form = ProfileChangeForm(instance=request.user)
    context = {
        'change_form' : change_form,
        'user_info' : user_info,
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    leave(request)
    return HttpResponseRedirect(reverse('main:index'))