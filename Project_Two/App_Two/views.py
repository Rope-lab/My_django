from django.shortcuts import render
from django.http import HttpResponse
from App_Two.models import Webpage, AccessRecord 

# Create your views here.
def index(request):
    #return HttpResponse('<em>My second app!</em>')
    webpages = Webpage.objects.all().values('topic__top_name','name','url','accessrecord__date')#django will automaticly look up the class related to the column
    my_dict = {
        'wbp': webpages,
    }
    return render(request,"App_Two_templates\index.html",my_dict)
def help(request):
    my_dict = {"insert_help":"Hello from views!"}
    return render(request,"App_Two_templates\help.html",context=my_dict)
def images(request):
    my_dict = {"insert_images":"Hello from views again!"}
    return render(request,"App_Two_templates\images.html",context=my_dict)