from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Customer


# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('home')


def register_or_login(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')

            user = User.objects.create_user(username=username, password=password, email=email)
            customer = Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address

            )
            message = 'User is registered successfully'
            messages.success(request, message)

        except Exception as e:
            error_message = 'Duplicate user or invalid inputs'
            messages.error(request, error_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid credentials'
            messages.error(request, error_message)

    return render(request, 'account.html', context)
