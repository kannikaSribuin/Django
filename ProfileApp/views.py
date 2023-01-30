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
    myproduct = [
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
    return render(request, 'profile/shop.html', {'myproduct': myproduct})
def etc(request):
    return render(request, 'profile/etc.html')

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