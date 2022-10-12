
from django.shortcuts import render, redirect
# import mysql.connector as sql
from .models import IlkmsUser
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

fn = ''
oc = ''
user_t = ''
em = ''
pwd = ''
pwd2 = ''


def SignUpaction(request):
 
    if request.method == 'POST':

        data = request.POST
        print(data)
        for key, value in data.items():
            if key == "full_name":
                fn = value
            if key == "occupation":
                oc = value
                print(oc)
            if key == "user_type":
                user_t = value
                print(user_t)
            if key == "email":
                em = value
            if key == "password":
                pwd = value
            if key == "password2":
                pwd2 = value

        # User(first_name=fn, last_name=ln, gender=s, email=em, password=pwd, password2=pwd2).save()
        user = IlkmsUser.objects.create_user(first_name=fn, occupation=oc, username=em, email=em, password=pwd, user_type=user_t)

        # user.user_type = user_t
        user.save()
        # print(user)
        messages.success(request, "Your account has been created successfully.")
        return redirect("login_page")
    else:
        # print(dir(IlkmsUser))
        return render(request, "ILKMS_project/signup.html")
