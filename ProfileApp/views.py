from ProfileApp.models import *
import datetime
from django.shortcuts import render, redirect
from ProfileApp.Form import *

# Create your views here.
def home(request):
    return render(request, 'home.html')
def myinfo(request):
    return render(request, 'Profile/Myinfo.html')
def education(request):
    return render(request, 'Profile/education.html')
def interest(request):
    return render(request, 'Profile/interest.html')
def career(request):
    return render(request, 'Profile/career.html')

listProduct = []
def shop(request):
    details = "fashion hat"
    name = "น.ส. กรรณิกา ศรีบุรินทร์"
    date = datetime.datetime.now()
    return render(request, 'Profile/shop.html', {'lstProduct': listProduct,
                                                'details': details, 'name': name,
                                                'date': date.strftime("%A %d-%m-%Y %H : %M")})
def inputPoduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            name = form.get('name')
            color = form.get('color')
            price = form.get('price')
            am = form.get('amount')
            size = form.get('size')
            pd = product(id, name, am, color, size, price)
            listProduct.append(pd)
            return redirect('shop')
        else:
            return redirect('pro_retrive_all')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'Profile/inputProduct.html', context)

    # pd1 = product("001", "JACQUEMUS Le bob Gadjo", "5", "-", "M", 100, 'images/s1.jpg')
    # pd2 = product("002", "PRADA Re-Nylon Bucket Hat", "10", "-", "M", 150, "images/s2.jpg")
    # pd3 = product("003", "RG-OO Qan-T", "6", "-", "L", 89, "images/pd3.jpg")
    # pd4 = product("004", "RG-Astray Gold FRAME", "8", "-", "L", 30, "images/s4.jpg")
    # pd5 = product("005", "MG-SINANJU", "5", "-", "M", 49, 'images/s5.jpg')
    # pd6 = product("006", "MG OO XN Raiser", "5", "-", "XL", 99, 'images/s6.jpg')
    # pd7 = product("007", "MG GUNDAM DEATHSCYTHE HELL", "10", "-", "S", 49, 'images/s7.jpg')
    # pd8 = product("008", "MG ZZ Gundam", "10", "-", "S", 200, 'images/s8.jpg')
    # pd9 = product("009", "MG Astray Blue Frame D", "10", "-", "M", 69, 'images/s9.jpg')
    # pd10 = product("010", "MG STRIKE FREEDOM", "10", "-", "M", 69, 'images/s10.jpg')
    # listProduct.append(pd1)
    # listProduct.append(pd2)
    # listProduct.append(pd3)
    # listProduct.append(pd4)
    # listProduct.append(pd5)
    # listProduct.append(pd6)
    # listProduct.append(pd7)
    # listProduct.append(pd8)
    # listProduct.append(pd9)
    # listProduct.append(pd10)
    # # return render(request, 'Profile/shop.html', {'product': listProduct,
    #                                      'details': details, 'name': name,
    #                                      'date': date.strftime("%A %d-%m-%Y %H : %M")})



def lab10(request):
    name = "กรรณิกา ศรีบุรินทร์์"
    stdid = "6534230202-1"
    address = "74 ม.3 ต.ท่าสะอาด อ.นาด้วง จ.เลย 42210"
    gen = "หญิง"
    weight = "50"
    height = "163"
    color = "สีดำ"
    food = "ชาบู"
    job = "นักศึกษา"
    productlist = [
                   ["JACQUEMUS Le bob Gadjo", 100, "images/s1.jpg"],
                   ["PRADA Re-Nylon Bucket Hat", 150, "images/s2.jpg"],
                   ["DIOR DIORESORT Small Brim Hat", 89, "images/pd3.jpg"],
                   ["GUCCI GG Canvas Bucket Hat", 30, "images/s4.jpg"],
                   ["CELINE Cotton Drill Baseball Cap", 49, "images/s5.jpg"],
                   ["BURBERRY Vintage Check Technical Cotton Bucket Hat", 99, "images/s6.jpg"],
                   ["PALM ANGELS Black Logo Cap", 49, "images/s7.jpg"],
                   ["FENDI Fendirama Hat", 200, "images/s8.jpg"],
                   ["LOEWE Bucket Hat in Anagram Jacquard and Calfskin", 69, "images/s9.jpg"],
                   ["CHANEL Cloche Hat", 69, "images/s10.jpg"],
                   ]
    return render(request, 'Profile/lab10.html',{'name': name, 'stdid': stdid, 'address': address, 'gen': gen,
                                              'weight': weight, 'height': height, 'color': color, 'food': food,
                                              'job': job, 'productlist': productlist})
