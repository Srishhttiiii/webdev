from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def home(request):
    # try:
    #     data = Specialskills.objects.all()
    #     context = {"special":data}
    # except Exception as e:
    #     context = {"special": "Not found"}
    return render(request,'index.html')

def support(request):
    return render(request,'support.html')

def meditation(request):
    return render(request,'meditation.html')

def journaling(request):
    return render(request,'journaling.html')

def timetable(request):
    return render(request,'timetable.html')

def therapy(request):
    return render(request,'therapy.html')

def contact(request):
    return render(request,'contact.html')

def blogs(request):
    try:
        data = Blog.objects.all()
        context = {"blo":data}
    except Exception as e:
        context = {"blo":"Data not found"}
    return render(request,'blog.html',context)


def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')