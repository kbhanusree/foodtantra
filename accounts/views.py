from django.shortcuts import redirect, render
from .models import accounts


def register(request):
    if request.method == 'POST':
        
            post = accounts()
            post.time = request.POST.get('time')
            post.date = request.POST.get('date')
            post.cuisine = request.POST.get('cuisine')
           
            post.email = request.POST.get('email')
            post.name = request.POST.get('name')
            post.people = request.POST.get('people')
            post.save()
            print(1)
            return render(request,'success.html')
        
    else:
            print(3)
            return render(request,'register.html')