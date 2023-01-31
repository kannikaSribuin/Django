from django.contrib import admin
from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myinfo', views.myinfo, name='myinfo'),
    path('education', views.education, name='education'),
    path('interest', views.interest, name='interest'),
    path('career', views.career, name='career'),
    path('lab10', views.lab10, name='lab10'),
    path('lab11', views.lab11, name='lab11'),

]