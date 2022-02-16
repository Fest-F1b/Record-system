from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# Create your views here.


def register(request):
     if request.method == 'POST':
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               messages.success(
               request, f'Hey {username} :) !, Account successfully Created, Login Here')
               return redirect('login')
     else:
          form = UserRegisterForm()
     return render(request, 'users/register.html',{'form':form})


def login1(request):
     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(request, username=username, password=password)
     if user is not None:
          login(request, user)
          messages.success(request, f'Succefully Logged In{username} !')
          return redirect('home')
     else:
          messages.warning(request, f'User is not registered')
     return render(request, 'users/login.html', {'user':user})


def logout_view(request):
     logout(request)
     messages.warning(request, f'Your have Logged out')
     return redirect('home')
