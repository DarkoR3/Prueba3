from django.shortcuts import render
import json
from .models import *


def home(request):
    navs = Navbar.objects.all()

    # print(navs)
    context = {
        'navs': navs
    }

    return render(request, 'core/home.html', context)


def services(request):
    navs = Navbar.objects.all()
    services = Service.objects.all()


    # print(navs)
    context = {
        'navs': navs,
        'services': services
    }
    return render(request, 'core/services.html', context)

def about(request):
    navs = Navbar.objects.all()
    about = About.objects.first()
    # staff = json.loads(about.staff)

    # print(navs)
    context = {
        'navs': navs,
        'about': about,
        # 'staff': staff
    }
    return render(request, 'core/about.html', context)