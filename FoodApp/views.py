from django.shortcuts import render
from . models import place

# Create your views here.
def fun(request):
    abc=place.objects.all()

    return render(request,"index.html",{'results':abc})

