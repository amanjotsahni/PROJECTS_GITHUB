from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Destination
from .models import book
from .forms import bookingform
from .forms import LoginForm
from .models import Login
from .models import Register
from .forms import RegisterForm

@csrf_exempt
def loginpage(request):
    if request.method == 'GET':
        return render(request,'login.html')
def login(request):
    if request.method == 'POST':

     a1=LoginForm(request.POST)
     Username=request.POST.get('username')
     Password=request.POST.get('password')
     context={
         'Username':Username,
         'Password':Password
     }
     login1=Login(Username=Username,Password=Password)
     login1.save()
     return redirect(request,'home.html',context)



def home(request):

         return render(request,'home.html')
def aboutus(request):
    return render(request,'aboutus.html')
def rooms(request):
 dests = Destination.objects.all()
 if (request.method == "POST"):
    return render(request,'bookingform.html')
 else:
     return render(request,'rooms.html',{'dests': dests})
def contactus(request):
    return render(request,'contactus.html')


def booking(request):
 if request.method == "GET":

    form = bookingform(request.GET)

    First=request.GET.get('First')
    Last=request.GET.get('Last')
    Phone=request.GET.get('Phone')
    Email=request.GET.get('Email')
    Arriving=request.GET.get('Arriving')
    Departure=request.GET.get('Departure')
    adults=request.GET.get('adults')
    children=request.GET.get('children')
    questions=request.GET.get('Questions')
    context = {
            'fname': First,
            'lname': Last,
            'phone': Phone,
            'email': Email,
            'arriving': Arriving,
            'departure': Departure,
            'adults': adults,
            'children': children,
            'questions': questions
        }
    book1 = book(First=First,Last=Last,Phone=Phone,Email=Email,Arriving=Arriving,Departure=Departure,adults=adults, children =children,questions=questions)
    book1.save()
    return render(request, "details.html", context)
def register(request):
    if request.method == "GET":
        form = RegisterForm(request.GET)

        uname = request.GET.get('uname')
        uemail = request.GET.get('uemail')
        upassword=request.GET.get('upassword')
        ure_password=request.GET.get('ure_password')
        context = {
            'uname': uname,
            'uemail': uemail,
            'upassword':upassword,
            'ure_password':ure_password
        }
        reg1 = Register(uname=uname, uemail=uemail,upassword=upassword,ure_password=ure_password)
        if upassword == ure_password:
         reg1.save()
         return redirect(request, '/home/', context)
        else:
            return render(request,'register.html',context)

def registerpage(request):
   return render(request,'register.html')



def testimonials(request):
    return render(request,'Testimonials.html')