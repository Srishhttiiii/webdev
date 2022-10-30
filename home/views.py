from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import RecForms, BlogForms
from .models import Blog, Rec, Therapy
from django.contrib.auth.decorators import login_required
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
     try:
        data = Therapy.objects.all()
        context = {"the":data}
     except Exception as e:
        context = {"the":"Data not found"}
     return render(request,'therapy.html',context)

def contact(request):
    return render(request,'contact.html')

def blogs(request):
    try:
        data = Blog.objects.all()
        context = {"blo":data}
    except Exception as e:
        context = {"blo":"Data not found"}
    return render(request,'blog.html',context)

def rec(request):
    try:
        data = Rec.objects.all()
        context = {"rec":data}
    except Exception as e:
        context = {"rec":"Data not found"}
    return render(request,'rec.html',context)


@login_required(login_url='loginPage')
def recAdd(request):
    form = RecForms()
    if request.method == 'POST':
        myData = RecForms(request.POST)
        if myData.is_valid():
            myData.save()
            messages.success(request, 'Recommendation Added Successfully')
            return redirect('rec')
    context = {"form":form}
    return render(request, 'recAdd.html', context)

@login_required(login_url='loginPage')
def recDelete(request, id):
    data = Rec.objects.get(id=id)
    data.delete()
    messages.warning(request, 'Recommendation Deleted Successfully')
    return redirect('rec')

@login_required(login_url='loginPage')
def recUpdate(request,id):
    myData = Rec.objects.get(id=id)
    updateForm = RecForms(request.POST or None, instance=myData)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request, 'Recommendation Updated Successfully')
        return redirect("rec")
    context = {"form":updateForm} 
    return render(request, 'recUpdate.html',context)