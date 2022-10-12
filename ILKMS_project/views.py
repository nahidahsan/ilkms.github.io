from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from chatbot.models import chatbot_history
data = chatbot_history.objects.values()
def homePage(request):
    return render(request, "ILKMS_project/home.html")

def homePage2(request):
    return render(request, "ILKMS_project/home2.html")

def Login(request):
    return render(request, "ILKMS_project/login.html")

def chatbot_st(request):
    return HttpResponseRedirect("http://165.22.214.160:8501")

def SignUp(request):
    return render(request, "ILKMS_project/signup.html")

# @login_required
def Dashboard(request):
    return render(request, "ILKMS_project/dashboard.html")

def archive(request):
    return render(request,'ILKMS_project/Archive.html')

def ebook(request):
    return render(request,'ILKMS_project/ebook.html')

def ebooklist(request):
    return render(request,'ILKMS_project/E-Book.html')

# def ocr(request):
#     return render(request, 'ILKMS_project/ocr.html')

def dashboard(request):
    return render(request, 'ILKMS_project/dashboard.html')

def editing(request):
    return render(request, 'ILKMS_project/editing.html')

def blog(request):
    return render(request, 'ILKMS_project/Blogs.html')

def approved(request):
    return render(request,'ILKMS_project/Archive_Approved.html')

def edit(request):
    return render(request,'ILKMS_project/EditPanel.html')

def newblog(request):
    return render(request,'ILKMS_project/New_Blogs.html')

def chatbot(request):
    return render(request, 'ILKMS_project/Chatbot.html')

def chatbot2(request):
    return render(request, 'ILKMS_project/Chatbot2.html')

def chatbot3(request):
    return render(request, 'ILKMS_project/Chatbot3.html')

def chatbot4(request):
    return render(request, 'ILKMS_project/Chatbot4.html')

def metainput(request):
    return render(request, 'ILKMS_project/Meta_Input.html')

def rolepermission(request):
    return render(request, 'ILKMS_project/RolePermission.html')

def notificationsetup(request):
    return render(request, 'ILKMS_project/NotificationSetup.html')

def userlist(request):
    return render(request, 'ILKMS_project/Userlist.html')


def chatbotUI(request):
    return render(request, 'ILKMS_project/chatbotUI.html')


def Homepage(request):
    return render(request, 'ILKMS_project/Homepage.html', {'data': data})

def ebook(request):
    return render(request, 'ILKMS_project/ebook.html')

def ebookread(request):
    return render(request, 'ILKMS_project/ebookread.html')

def ebookcomments(request):
    return render(request, 'ILKMS_project/ebookcomments.html')