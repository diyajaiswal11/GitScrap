import requests
from django.shortcuts import render



def home(request):
    if request.method=='GET':
        username=request.GET['username']
        url='https://api.github.com/users/%s' %username
        response=requests.get(url)
        user=response.json()
        #idofuser=user.id
        #profilepic='https://avatars3.githubusercontent.com/u/%s?v=4' %idofuser
    return render(request,'home.html',{'user':user})