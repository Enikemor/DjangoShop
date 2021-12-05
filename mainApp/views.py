from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from mainApp.models import Users

# Create your views here.
from requests import auth


def index(request):
    return render(request,'login.html')

def register(request):

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = Users.objects.create_user(username=username, password=password, email=email)
        user.save()

        auth.login(request, user)
        return HttpResponseRedirect("")

    return render(request, 'registration.html')

def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("")

    return render(request, 'login.html')




