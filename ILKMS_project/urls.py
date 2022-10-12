"""ILKMS_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from ILKMS_project import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from SignUp.views import SignUpaction
from login.views import loginaction, display
from chatbot.views import chatbot_res


urlpatterns = [
    path("admin/", admin.site.urls),
    path("homepage", views.homePage, name="homepage"),
    path("", views.Homepage, name="home"),
    path("chatbotst", views.chatbot_st, name="chatbot"),
    path("ebook", views.ebook, name="ebook"),
    path("ebookread", views.ebookread, name="ebookread"),
    path("ebookcomments", views.ebookcomments, name="ebookcomments"),
    path("Sign_Up", SignUpaction, name="SignUp"),
    # path("dashboard/", views.Dashboard, name="dashboard"),
    path("Sign_In", loginaction, name="login_page"),
    path("display", display, name="display"),
    # path('ocr/', views.ocr, name = "OCR"),
    # path('archive/', views.archive, name = "archive"),
    # path('ebook/', views.ebook, name = "ebook"),
    # path('ebooklist/', views.ebooklist, name = "ebooklist"),
    # path('editing/', views.editing, name="editing"),
    # path('blog/', views.blog, name="blog"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('dashboard/', views.dashboard),
    # path('ocr/', views.ocr, name = "OCR"),
    path('archive/', views.archive),
    path('approved/', views.approved),
    path('edit/', views.edit),
    path('metainput/', views.metainput),
    path('ebooklist/', views.ebooklist),
    path('blog/', views.blog),
    path('newblog/', views.newblog),
    path('chatbot/', views.chatbot),
    path('chatbot2/', views.chatbot2),
    path('chatbot3/', views.chatbot3),
    path('chatbot4/', views.chatbot4),
    # path('homepage/', views.homepage),
    path('rolepermission/', views.rolepermission),
    path('notificationsetup/', views.notificationsetup),
    path('userlist/', views.userlist),
    path("chatbotUI", chatbot_res, name="chatbotUI"),
    path('', include('ocr.urls')),   

]

urlpatterns += staticfiles_urlpatterns()
