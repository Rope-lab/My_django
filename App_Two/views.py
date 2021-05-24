from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<em>My second app!</em>')
def help(request):
    my_dict = {"insert_help":"Hello from views!"}
    return render(request,"help.html",context=my_dict)
    

