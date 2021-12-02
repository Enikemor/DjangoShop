from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home1.html')

def register(request):

    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            return HttpResponseRedirect("/books/")
    else:
        data, errors = {}, {}

    return render(request,"registration/register.html")
