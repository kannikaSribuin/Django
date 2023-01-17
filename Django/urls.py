from django.contrib import admin
from django.urls import path
from django.urls import path, include
from ProfileApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('ProfileApp/', include('ProfileApp.urls')),

]
