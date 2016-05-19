from django.shortcuts import render

from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

@login_required
def user_home(request):
    """ homepage for a user after they've logged in """
    return render(request, 'user_home.html')

@login_required
def gleanlist(request):
    """ user list of all gleans """
    return render(request, 'gleanlist.html')
