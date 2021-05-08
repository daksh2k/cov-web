from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages, auth
from django.contrib.auth.models import User
from users.models import Users
from requirement.models import Requirement
from donation.models import Donation
from .forms import DonationForm

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

    requirements = Requirement.objects.order_by('name').filter(is_satisfied=False)
    context = {
        'requirements': requirements
    }
    return render(request, 'users/dashboard.html', context)

def viewrequirement(request, requirement_id):
    viewed_requirement = Requirement.objects.get(id = requirement_id)
    context = {
        'viewed_requirement': viewed_requirement
    }
    return render(request, 'users/viewrequirement.html', context)

def donate(request, requirement_id):
    # # if request.method != 'POST':
    # if requirement_id != 0:
    requirement = Requirement.objects.get(id = requirement_id)
    # print(requirement.ngos.name)
    # initial_dict = { 
    #     "ngos" : requirement.ngos
    # } 

    form = DonationForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.users = request.user.users
        # instance.ngos = requirement.ngos
        instance.save()
        form = DonationForm()
        # return redirect('userdashboard')

    context = {
        'form': form
    }
    return render(request, 'users/donate.html', context)

class DonateView(View):
    
    def get(self, request, **kwargs):
        request.session['myid'] = self.kwargs['requirement_id']
        form = DonationForm()
        context = {
        'form': form
        }
        return render(request, 'users/donate.html', context)
    
    def post(self, request, **kwargs):
        requirement = Requirement.objects.get(id = request.session['myid'])
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.users = request.user.users
            instance.ngos = requirement.ngos
            instance.save()
            messages.success(request, 'Equipment Donated')

        # context = {
        # 'form': form
        # }
        return redirect('userdashboard')

def donations(request):
    pending_donations = Donation.objects.order_by('name').filter(users=request.user.users ,is_completed=False)
    completed_donations = Donation.objects.order_by('name').filter(users=request.user.users ,is_completed=True)
    context = {
        'completed_donations': completed_donations,
        'pending_donations': pending_donations
    }
    return render(request, 'users/donations.html', context)    

def viewdonation(request, donation_id):
    viewed_donation = Donation.objects.get(id = donation_id)
    context = {
        'viewed_donation': viewed_donation
    }
    return render(request, 'users/viewdonation.html', context)