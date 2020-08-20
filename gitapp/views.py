import requests
from django.shortcuts import render

def home(request):
    return render(request,'index.html')


def detail(request):
    if request.method=='GET':
       username=request.GET['username']
       user=requests.get('https://api.github.com/users/%s' % username).json()
       repos=requests.get('https://api.github.com/users/%s/repos?page=1&per_page=100&sort=updated' %username).json()
       #print(user.blog)
      
 
    return render(request,'profile.html',{'user':user, 'repos':repos })