from django.shortcuts import render
from .models import cuisine
# Create your views here.
def index(request):

    cus = cuisine.objects.all()

    return render(request,'index.html',{'cus' : cus})