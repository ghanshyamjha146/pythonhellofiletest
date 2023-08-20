from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


#test function
def test(request):
    print(request,"test===========")
    return HttpResponse("Hi this is test")


#Home Page.
# login_required()
@login_required(login_url='/mobile/login')
def home(request):
    return render(request,'home_page.html')

#Signup Page.
def signup(request):
    user_data = request.POST
    if request.method == 'POST':
        name = user_data.get('name')
        email = user_data.get('email')
        password = user_data.get('password')
        confirm_pass = user_data.get('confirm_password')

        try:
            user_check = User.objects.get(username = email)
            if user_check:
                check_usr = "This Email Is Already Exists Please Enter Unique Email:"
                return render(request,"signup.html",{'check_usr': check_usr})
        except:
            pass
        if password==confirm_pass:
            user = User.objects.create_user(name = name, username = email, password = confirm_pass, email = email)

            # user.set_password(password)
            # user.save()

        else:
            msg = "Password and confirm password not matched"
            return render(request, "signup.html",{'msg':msg})
        return redirect('/mobile/login')

    return render(request,"signup.html")


#Login Page.
def user_login(request):

    user_data = request.POST
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        email = user_data.get('email')
        password = user_data.get('password')
        user = authenticate(username=email, password=password)
        print(user,"55555555555555555")
        if user is not None:
            login(request, user)
            return redirect('/mobile/user_page')
        else:
            msg= "Please enter valid email and password:"
            return render(request,'login.html',{'msg':msg})

    return render(request,"login.html")


#About Page.
def about(request):
    return render(request,"about.html")

#User Page.
def user_page(request):
    return render(request,"user_page.html")

#Logout Function.
def logout_view(request):
    logout(request)
    return redirect('/mobile/home')








