from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
import os
from django.core.files.storage import FileSystemStorage
import json
from financepeertask import models


def index(request):
    return render(request, 'index.html')


def register(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def getFile(request):
    fileObj = request.FILES['filePath']
    fsObj = FileSystemStorage()
    filePathName = fsObj.save(fileObj.name, fileObj)
    filePathName = fsObj.url(filePathName)
    filename = filePathName[7:]
    filePathName = '.' + filePathName
    filePathName = filePathName.replace("%", " ")
    with open(filePathName) as f:
        data = json.load(f)
        for entry in data:
            print(entry['userId'])
            det = models.Details()
            det.userId = entry['userId']
            det.id1 = entry['id']
            det.title = entry['title']
            det.body = entry['body']
            det.save()
    data = models.Details.objects.all()
    return render(request, 'done.html')


def showData(request):
    data = models.Details.objects.all()
    print(data)
    return render(request, 'show.html', {"Details": data})


def logout(request):
    return redirect('http://127.0.0.1:8000/accounts/logout')


def login(request):
    return redirect('http://127.0.0.1:8000/accounts/login')
