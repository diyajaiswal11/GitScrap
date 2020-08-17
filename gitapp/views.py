import requests
from django.shortcuts import render

def home(request):
    return render(request,'index.html')


def detail(request):
    if request.method=='GET':
       username=request.GET['username']
       user=requests.get('https://api.github.com/users/%s' % username).json()
       repos=requests.get('https://api.github.com/users/%s/repos' %username).json()
      
 
    return render(request,'profile.html',{'user':user, 'repos':repos})