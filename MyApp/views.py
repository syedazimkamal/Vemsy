from django.http import HttpResponse, request, response
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UsernameField
from django.urls.conf import include
from .forms import CreateUserForm, Help
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Help
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'index.html')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('first_name')
                messages.success(request, username + ' you are successfully registered!')
                return redirect('sign_in')

        context = {'form':form}
        return render(request, 'sign_up.html', context)
    
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect.')

        return render(request, 'sign_in.html')

def sign_out(request):
    logout(request)
    return redirect('sign_in')

@login_required(login_url='sign_in')
def home(request):
    if request.method == "POST":
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        company = request.POST.get('company')
        c_model = request.POST.get('c_model')
        issue = request.POST.get('issue')
        phone = request.POST.get('number')
        o_issue = request.POST.get('o_issue')

        home = Help(latitude=latitude, longitude=longitude, company=company, c_model=c_model, issue=issue, o_issue=o_issue, phone=phone, helpTime = datetime.today())
        home.user = request.user
        home.save()

        return redirect('helping', issue=issue, latitude=latitude, longitude=longitude)
    return render(request, 'home.html')

def helping(request, issue, latitude, longitude):
    myIssue = "Issues\%s.html" % issue
    context = {
        'Issue':myIssue,
        'latitude':latitude,
        'longitude':longitude,
    }
    return render(request,'helping.html', context)

def ac_lights(request):
    return render(request, 'issues/ac_lights.html')

def break_pad_worn(request):
    return render(request, 'issues/break_pad_worn.html')

def dead_battery(request):
    return render(request, 'issues/dead_battery.html')

def engine_issue(request):
    return render(request, 'issues/engine_issue.html')

def engine_overheat(request):
    return render(request, 'issues/engine_overheat.html')

def flat_tyres(request):
    return render(request, 'issues/flat_tyres.html')

def fuel_leak(request):
    return render(request, 'issues/fuel_leak.html')

def no_fuel(request):
    return render(request, 'issues/no_fuel.html')

def others(request):
    return render(request, 'issues/others.html')

def uneven_tyre(request):
    return render(request, 'issues/uneven_tyre.html')

def warning(request):
    return render(request, 'issues/warning.html')
