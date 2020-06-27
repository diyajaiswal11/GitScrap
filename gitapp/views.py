import requests
from django.shortcuts import render



def home(request):
    if request.method=='GET':
        username=request.GET['username']
        user=requests.get('https://api.github.com/users/%s' % username).json()
        repos=requests.get('https://api.github.com/users/%s/repos' %username).json()
        l=[]
        commit=len(requests.get('https://api.github.com/repos/%s/%s/commits' % (username ,repos[0]["name"])).json())
        print(commit)
        
        #print(repos)
        #idofuser=user.id
        #profilepic='https://avatars3.githubusercontent.com/u/%s?v=4' %idofuser
    return render(request,'home.html',{'user':user, 'repos':repos})