from email import message
from http.client import HTTPResponse
from django.shortcuts import render, redirect

# import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth import authenticate, login
from SignUp.models import IlkmsUser
#from django.contrib.auth.models import IlkmsUser
# Create your views here.
from chatbot.models import chatbot_history

email = ''
password = ''


def loginaction(request):

    if request.method == "POST":
        email = request.POST['email']
        # print(email)
        password = request.POST['password']
        # print(password)

        # user = None
        # for i in st.values('email', 'password'):
        #     print(i["email"], i["password"], email, password)
        #     if i["email"] == email and i["password"] == password:
        #         user = "authenticated"
        #         break
        #     else:
        #         user = None

        user = authenticate(username=email, password=password)
        # print(type(user.ilkmsuser.user_type))

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.success(request, 'ভূল তথ্য!! পুনরায় চেষ্টা করুন..')
            return redirect("login_page")
            # return render(request, "ILKMS_project/login.html", {'error': 'ভূল তথ্য!! পুনরায় চেষ্টা করুন..'})
    else:

        return render(request, "ILKMS_project/login.html")


def display(request):
    st = chatbot_history.objects.all()   # Collect all records from table
    return render(request, 'ILKMS_project/display.html', {'st': st})
