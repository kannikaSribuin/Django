from datetime import datetime

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
def shop(request):
    details = "Gundam plastic model (Gunpla)"
    name = "น.ส. กรรณิกา ศรีบุรินทร์"
    date = datetime.datetime.now()

    product = []
    pd1 = product("001", "RG-Wing Gundam Zero EW", "1/144", "RG", "12-13cm", 915, 'images/.jpg')
    pd2 = product("002", "RG-Unicorn Gundam", "1/144", "RG", "12-13cm", 1395, "images/.jpg")
    pd3 = product("003", "RG-OO Qan-T", "1/144", "RG", "12-13cm", 915, "images/OO-q.jpg")
    pd4 = product("004", "RG-Astray Gold FRAME", "1/144", "RG", "12-13cm", 1098, "images/astray.jpg")
    pd5 = product("005", "MG-SINANJU", "1/100", "MG", "17-18cm", 2752, 'images/sinanju.jpg')
    pd6 = product("006", "MG OO XN Raiser", "1/100", "MG", "17-18cm", 2960, 'images/oo-xn.jpg')
    pd7 = product("007", "MG GUNDAM DEATHSCYTHE HELL", "1/100", "MG", "17-18cm", 1653, 'images/deathscythe.jpg')
    pd8 = product("008", "MG ZZ Gundam", "1/100", "MG", "17-18cm", 2220, 'images/zz-gundam.jpg')
    pd9 = product("009", "MG Astray Blue Frame D", "1/100", "MG", "17-18cm", 1772, 'images/blueframe.jpg')
    pd10 = product("010", "MG STRIKE FREEDOM", "1/100", "MG", "17-18cm", 2564, 'images/strike.jpg')
    product.append(pd1)
    product.append(pd2)
    product.append(pd3)
    product.append(pd4)
    product.append(pd5)
    product.append(pd6)
    product.append(pd7)
    product.append(pd8)
    product.append(pd9)
    product.append(pd10)
    return render(request, 'shop.html', {'product': product,
                                         'details': details, 'name': name,
                                         'date': date.strftime("%A %d-%m-%Y %H : %M")})

  

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
