"""cricket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from testapp.views import StudentSignUpView,login,Student_details_api,Updatestudentsubject,Updatestudentsubject,reportview
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token,refresh_jwt_token

from rest_framework import routers
router = routers.DefaultRouter()
# # router.register(r'st', Student_details_api, basename='st')
# updating student api
router.register(r'update', Updatestudentsubject,basename='teacher')
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^signup/',StudentSignUpView.as_view()),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'login/',login),
    # get JWT token based on student
    url('api/jwt/obtaine/',obtain_jwt_token),
    # url('api/jwt/verify/',obtain_jwt_token),
    # url('api/jwt/refresh/',obtain_jwt_token),
    # GETTING STUDENT INFO
    url(r'^jwt/student/', Student_details_api.as_view()),
    url('api/', include(router.urls)),
    # Generating report as tabular formate
    url(r'^report/',reportview.as_view())
]



