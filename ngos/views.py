from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from ngos.models import Ngos
from requirement.models import Requirement


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('ngodashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('ngologin')
    else:
        return render(request, 'ngos/login.html')


def register(request):
    if request.method == 'POST':
        #Get form values
        name = request.POST['name']
        username = request.POST['user_name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        pincode = request.POST['pincode']
        phone = request.POST['phone']
        registration_no = request.POST['registration_number']
        certificate = request.POST['certificate']
        website = request.POST['website']
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
                ngo = Ngos(user = user, name = name, email = email, address = address, city = city, pincode = pincode, phone = phone, registration_no = registration_no, certificate = certificate, website = website)
                ngo.save()
                # user.ngos.name = name
                # user.ngos.email = email
                # user.ngos.address = address
                # user.ngos.city = city
                # user.ngos.pincode = pincode
                # user.ngos.phone = phone
                # user.ngos.registration_no = registration_no
                # user.ngos.certificate = certificate
                # user.ngos.website = website
                messages.success(request, 'You are now registered and can log in')
                return redirect('ngologin')   
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('ngoregister')

    else:
        return render(request, 'ngos/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'ngos/dashboard.html')

def requirements(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        description = request.POST['description']
        photo = request.POST['photo']
        


    return render(request, 'ngos/requirements.html')    