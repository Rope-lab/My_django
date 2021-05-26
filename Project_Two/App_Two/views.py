from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<em>My second app!</em>')
    return render(request,"App_Two_templates\index.html")
def help(request):
    my_dict = {"insert_help":"Hello from views!"}
    return render(request,"App_Two_templates\help.html",context=my_dict)
def images(request):
    my_dict = {"insert_images":"Hello from views again!"}
    return render(request,"App_Two_templates\images.html",context=my_dict)