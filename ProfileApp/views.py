from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def myinfo(request):
    return render(request, 'profile/Myinfo.html')
def education(request):
    return render(request, 'profile/education.html')
def interest(request):
    return render(request, 'profile/interest.html')
def career(request):
    return render(request, 'profile/career.html')
def myidols(request):
    return render(request, 'profile/idol.html')
def etc(request):
    return render(request, 'profile/etc.html')