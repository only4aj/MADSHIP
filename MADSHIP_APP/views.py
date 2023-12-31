from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse
from .models import Customer,ProductItem,customerdetail,ContactForm
# from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib import messages, auth
from django.contrib.auth.models import User
import razorpay
from django.conf import settings
# from .models import Customer
# Create your views here.

@login_required(login_url='login')
def home(request):
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    return render(request, "index.html")

@login_required(login_url='login')
def mens_fashion(request):
    data = ProductItem.objects.all()
    return render(request,'items1.html',{'data':data})

@login_required(login_url='login')
def electronics(request):
    data = ProductItem.objects.all()
    return render(request,'items2.html',{'data':data})

@login_required(login_url='login')
def shoes(request):
    data = ProductItem.objects.all()
    return render(request,'items3.html',{'data':data})

@login_required(login_url='login')
def womens_fashion(request):
    data = ProductItem.objects.all()
    return render(request,'items4.html',{'data':data})

# def login(request):
#     username = str(request.POST.get('username'))
#     passwrd = str(request.POST.get('pass'))
#     if username == '' or passwrd == '':
#         return render(request,'login.html',{'error':''})
#     else:
#         # getdata = Customer.objects.filter()
#         getdata = Customer.objects.all()
#         for data in getdata:
#             if data.username == username and data.password == passwrd:
#                 return render(request, "index.html")
#         return render(request,'login.html',{'error':'Invalid Username or Password'})


@login_required(login_url='login')
def store(request):
    return render(request, "store.html")


@login_required(login_url='login')
def about(request):
    return render(request, "about.html")


# @login_required(login_url='login_success')
# def contact(request):
#     return render(request, "contact.html")

# def register(request):
#     return render(request, "register.html")

# def login(request):
#     return render(request, "login.html",{'error':''})


@login_required(login_url='login')
def cart(request):
    return render(request, "cart.html")

def term(request):
    return render(request,'terms.html')


def register(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        passwrd = request.POST.get('pass')


        if (usern == '' or email == '' or phone == '' or passwrd == ''):
            return render(request, 'register.html')

        else:
            user = User.objects.create_user(username=usern, email=email, password=passwrd)
        
            user.save()
            print("user created!")
            return redirect('/')

    #     if usern == '' or email == '' or phone == '' or passwrd == '':
    #         return render(request, "register.html")

    #     # Create a new customer account
    #     data = Customer(username=usern, PNumber=phone, email=email, password=passwrd)
    #     data.save()

    #     return render(request, 'login.html')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, "invalid credentials")
            return redirect("/")

        # if username == '' or password == '':
        #     return render(request, 'login.html', {'error': 'Please enter both username and password.'})

        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home')
        # else:
        #     messages.error(request, 'Invalid credentials')

    else:
        return render(request, 'login.html')


def LogOut(request):
    auth.logout(request)
    return redirect("/")



@login_required(login_url='login')
def product_view(request):
    itemId = request.POST.get('id')
    data = ProductItem.objects.all()
    for i in data:
        if str(i.item_id) == itemId:
            return render(request,'product.html',{'data':i})
    return render(request,'product.html',{'data':"error"})


# def checkout(request):
#     cstmrname = (request.POST.get('cstmrname'))
#     cstmremail = (request.POST.get("cstmremail"))
#     cstmraddress = (request.POST.get("cstmraddress"))
#     cstmrphone = request.POST.get("cstmrphone")
#     cstmrnpincode = request.POST.get("cstmrnpincode")

#     if(cstmrname == "" or cstmremail == "" or cstmraddress == "" or cstmrphone == '' or cstmrnpincode == ''):
#         return render(request,'checkout.html')
#     customerdata = customerdetail(name=cstmrname, mail=cstmremail, address=cstmraddress, mobile=(cstmrphone), pincode=(cstmrnpincode))
#     customerdata.save()
#     return render(request,'checkout.html')


@login_required(login_url='login')
def checkout(request):
    if request.method == 'POST':
        cstmrname = request.POST.get('name', '')
        cstmremail = request.POST.get('mail', '')
        cstmraddress = request.POST.get('address', '')
        amount = request.POST.get('amount', '0')
        cstmrphone = request.POST.get('mobile', '')
        cstmrpincode = request.POST.get('pincode', '')
        
        print(amount)
        if not (cstmrname and cstmremail and cstmraddress and cstmrphone and cstmrpincode):
            return render(request, 'checkout.html')

        customerdata = customerdetail(name=cstmrname, mail=cstmremail, address=cstmraddress, mobile=cstmrphone, pincode=cstmrpincode,amount=amount)
        customerdata.save()

        id = customerdata.id
        client = razorpay.Client(auth=("rzp_test_lCl3lgTUtrCbDN", "CqTKV9gjOUOqellCriobMF7b"))
        try:
            # amount = 10000
            order = client.order.create({'amount': int(amount)*100, 'currency': 'INR', 'payment_capture': 1})
        except Exception as e:
            return JsonResponse({'message': 'Error creating Razorpay order'})

        return JsonResponse({'order_id': order.get('id'), 'amount': order.get('amount')})

    return render(request, 'checkout.html')


@login_required(login_url='login')
def contact(request):

    message = None
    clear_form = False

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        usremail = request.POST.get('usremail')
        description = request.POST.get('description')

        if not (firstname and lastname and usremail and description):
            message = 'Please fill out all fields.'
        else:
            contactdata = ContactForm(fname=firstname, lname=lastname, email=usremail, desc=description)
            contactdata.save()
            message = 'Thanks for contacting us! We will reach you soon...'
            clear_form = True

    return render(request, 'contact.html', {'message': message, 'clear_form': clear_form})
