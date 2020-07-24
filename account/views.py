from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth.forms import UserCreationForm


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'base/base.html')
    else:
        return redirect('user-login')


def user_login(request):
    form = UserLoginForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            context={
                'form': form,
                'error': 'Invalid Username or Password !!'
            }
            return render(request,'account/loginlatest.html',context)
    return render(request,'account/loginlatest.html',context)


def user_logout(request):
    logout(request)
    return redirect('user-login')


def user_signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    context = {
        'form':form
    }
    return render(request,'account/register.html',context)

