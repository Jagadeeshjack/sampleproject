"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp.views import homePage, aboutPage, coursePage, addEnquiry, staffPage
from myapp.views import viewEnquiries, editPage, deletePage, AddStudent, ViewStudents
from myapp.views import EditStudent, DeleteStudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage),
    path('about/',aboutPage),
    path('course/',coursePage),
    path('enquiry/',addEnquiry),
    path('staff/',staffPage,name='staff'),
    path('staff/view/',viewEnquiries),
    path('staff/view/edit/<id>/',editPage),
    path('staff/view/delete/<id>/',deletePage),
    path('staff/add/',AddStudent.as_view(),name='addStu'),
    path('staff/students/',ViewStudents.as_view(),name='viewStu'),
    path('staff/students/edit/<id>/',EditStudent.as_view()),
    path('staff/students/delete/<id>/',DeleteStudent.as_view())
]

