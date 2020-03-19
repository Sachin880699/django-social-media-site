from django.shortcuts import render,redirect
from.models import *
from.forms import *
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
    username = None
    if request.user.is_authenticated :
        username = request.user.username

    return render(request,'home.html',{"username":username})






def login(request):
    if request.method == 'POST' and 'login' in request.POST:
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect!'})

    if request.method == 'POST' and 'signup' in request.POST:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'login.html', {'error':'Username is already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],request.POST['lastname'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')

    else:
        return render(request, 'login.html', {'error':'Password doesn\'t matched'})


    return render(request, 'login.html')


def profile(request):

    username = None
    if request.user.is_authenticated:
        username = request.user.username
        profile_image = Profile.objects.all()

    #----------------------------
    return render(request,'profile.html',{"username":username,'profile_image':profile_image})

def fillprofile(request):
    if request.method=='POST':

        data = Profile()
        data.nick_name = request.POST['nick_name']
        data.hobby = request.POST['hobby']
        data.profile_picture = request.FILES['profile_picture']
        data.status = request.POST['status']
        data.gender = request.POST['gender']
        data.relationship_status = request.POST['relationship_status']
        data.phone = request.POST['phone']
        data.save()

    else:
        pass
    return render(request,'fillprofile.html')