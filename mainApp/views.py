from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from mainApp.models import Users,Cart,Product

# Create your views here.
from django.contrib import auth


def index(request):
    # return render(request,'login.html')
    return render(request,'login.html')

def register(request):

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = Users.objects.create_user(username=username, password=password, email=email)
        user.save()

        auth.login(request, user)
        return HttpResponseRedirect("/product_list")

    return render(request, 'registration.html')

def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/product_list")

    return render(request, 'login.html')

def show_cart(request):
    user = request.user
    products = Cart.objects.filter(User = user)

    return render(request, 'chekout_extended.html', {'products': products})

def add_to_cart(request, id):
    user = request.user
    product = Product.objects.get(id = id)
    cart = Cart(ProdList = product, Users = user)
    cart.save()

    return render(request, '')


def delete_product(request, id):
    user = request.user
    product = Product.objects.get(id = id)
    product = Cart.objects.get(User = user, ProdList = product)

    return render(request, '')




