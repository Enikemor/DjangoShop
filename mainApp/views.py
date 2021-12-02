from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home1.html')

def register(request):

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, password=password, email=email)
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

def 


