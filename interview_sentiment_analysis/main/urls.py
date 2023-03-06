from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
        path("",views.main,name='main'),
        path("upload_file/",views.upload_file, name='upload_file'),

]
