from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from users.models import Users

def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('userdashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('userlogin')
    else:
        return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        pincode = request.POST['pincode']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if passwords match
        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('ngoregister')
            else:
                # Looks Good
                user = User.objects.create_user(username=username, password=password)
                user.save()
                u = Users(user = user, first_name = first_name, last_name=last_name, email = email, address = address, city = city, pincode = pincode, phone = phone)
                u.save()
                messages.success(request, 'You are now registered and can log in')
                return redirect('userregister')   
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('userregister')

    else:
        return render(request, 'users/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'users/dashboard.html')

def donations(request):
    return render(request, 'users/donations.html')    
