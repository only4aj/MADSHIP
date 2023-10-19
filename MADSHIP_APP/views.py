from django.shortcuts import render,HttpResponse
from .models import Customer,ProductItem
# from .models import Customer
# Create your views here.
def index(request):
    return render(request, "index.html")

def items1(request):
    data = ProductItem.objects.all()
    return render(request,'items1.html',{'data':data})

def items2(request):
    data = ProductItem.objects.all()
    return render(request,'items2.html',{'data':data})

def items3(request):
    data = ProductItem.objects.all()
    return render(request,'items3.html',{'data':data})

def items4(request):
    data = ProductItem.objects.all()
    return render(request,'items4.html',{'data':data})

def home(request):
    username = str(request.POST.get('username'))
    passwrd = str(request.POST.get('pass'))
    if username == '' or passwrd == '':
        return render(request,'login.html',{'error':''})
    else:
        # getdata = Customer.objects.filter()
        getdata = Customer.objects.all()
        for data in getdata:
            if data.username == username and data.password == passwrd:
                return render(request, "index.html")
        return render(request,'login.html',{'error':'Invalid Username or Password'})


def store(request):
    return render(request, "store.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html",{'error':''})

def cart(request):
    return render(request, "cart.html")

def term(request):
    return render(request,'terms.html')

def verification(request):
    usern = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    passwrd = request.POST.get('pass')

    if( usern == '' or email == '' or phone == '' or passwrd == ''):
        return render(request, "register.html")
    data = Customer(username = usern,PNumber=phone,email=email,password=passwrd)
    data.save()
    return render(request,'login.html',{'error':''})

def random(request):
    item_name = request.POST.get('id')
    data = ProductItem.objects.all()
    return render(request,'random.html',{'item':item_name,'data':data})
