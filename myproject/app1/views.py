from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from .models import RegStore, ContactDetails
from django.views.decorators.csrf import csrf_exempt  # import


# Create your views here.


def home_page(request):
    return render(request, 'home1.html')


'''def home(request):
    return render(request, 'home.html')'''


def login(request):
    return render(request, 'login.html')


def newuser(request):
    return render(request, 'registrationform.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def aboutaqua(request):
    return render(request, 'aboutagri.html')


def aboutagri(request):
    return render(request, 'aboutaqua.html')


def contactus(request):
    return render(request, 'enquiry.html')


def module1(request):
    return render(request, 'module1.html')


def module2(request):
    return render(request, 'module2.html')


def module3(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'index1.html')

def rate(request):
    return render(request, 'rate.html')

@csrf_exempt
def regdetails(request):
    uname = request.POST['username']
    password = request.POST['pwd']
    email = request.POST['email']
    mobile = request.POST['mobile']
    user = RegStore.objects.create(username=uname, password=password, email=email, phone=mobile)
    user.save();
    print("user created")
    return redirect('/')


@csrf_exempt
def contactdetails(request):
    name = request.POST['name']
    gmail = request.POST['gmail']
    mobile = request.POST['mobile']
    service = request.POST['service']
    user1 = ContactDetails.objects.create(name=name, gmail=gmail, phone=mobile, service=service)
    user1.save();
    print("available soon..request received")
    return redirect("/")
