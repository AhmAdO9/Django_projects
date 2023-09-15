from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from .models import Person,Blog,Draft,Appointment
from django.http import HttpResponse
from datetime import timedelta
from datetime import datetime


def signin(request):
    Username = request.POST.get("textX")
    signin.U = Username
    Pass = request.POST.get("textY")
    signin.P = Pass
    Category = (request.POST.get("Category")).lower()
    if request.POST.get("catehor"):
        blog_category = request.POST.get("catehor").lower()
        signin.blc = blog_category
    


    if request.POST.get("dp1"):
         Dp = request.POST.get("dp1")
         person = Person.objects.all()
         for i in person:
             if i.Username == Username:
                 i.Dp = Dp
                 i.save()
    else:
         pass
    user = authenticate(username=Username, password=Pass)
    if user:
        login(request, user)
        person = Person.objects.filter(Username=Username, Category=Category)
        if person:
            pass
        else:
            messages.error(request, "please type your category correctly!")
            return render(request, "signin.html")
        if Category == "patient":
            
            obj = Blog.objects.filter(Categories = blog_category)
            pers = Person.objects.filter(Category='doctor')
            if obj:
                pass
            blgs = []
            for i in obj:
                blgs.append(i)
            person = Person.objects.filter(Username=Username)
            return render(request, "Patient.html", {"person": person,"blgs":blgs,"pers":pers})
        else:
            person = Person.objects.filter(Username=Username)
            all_drafts = []
            objct = Draft.objects.all()
            for i in objct:
                all_drafts.append(i.Title)
     
            return render(request, "Doctor.html", {"person": person, "all_drafts":all_drafts})

    else:
        messages.error(request, "Bad credentials")
        return render(request, "signin.html")


def basic(request):
    return render(request, "signin.html")


def basic2(request):
    return render(request, "signup.html")


def signup(request):
    try:
        Username = request.POST.get("text0")
        Name = request.POST.get("text1")
        Last_name = request.POST.get("text2")
        Email = request.POST.get("text3")
        Pass = request.POST.get("text4")
        CPass = request.POST.get("text5")
        Category = request.POST.get("text6").lower()
        Address = request.POST.get("text7")
        Address2 = request.POST.get("text8", "default")
        
        if request.POST.get("text200") == "":
            Speciality = "Unregistered"
        else:
            Speciality= request.POST.get("text200")
            

        if request.POST.get("dp"):
            Dp = request.POST.get("dp")
        else:
            Dp="images.jpeg"
        
        try:
            if int(Name):
                messages.error(
                    request, "Please avoid numerical values wherever uneccessary!")
                return render(request, "signup.html")
        except ValueError:
            pass
        try:
            if int(Last_name):
                messages.error(
                    request, "Please avoid numerical values wherever uneccessary!")
                return render(request, "signup.html")
        except ValueError:
            pass

        if Pass != CPass:
            messages.error(request, "Password Match error!")
            return render(request, "signup.html")
        if len(Username) < 2 or len(Name) < 2 or len(Last_name) < 2 or len(Email) < 2 or len(Address) < 2 or len(Address2) < 2:
            messages.error(request, "please fill the form correctly")
            return render(request, "signup.html")
        if len(Pass) < 6:
            messages.error(request, "password length should be atleast 6")
            return render(request, "signup.html")

        person = Person(Username=Username, First_name=Name, Email=Email,
                        Last_name=Last_name, Address=Address, Category=Category, Password=Pass, Dp=Dp, Speciality=Speciality)
        person.save()
        user = User.objects.create_user(
            username=Username, email=Email, password=Pass)
        user.save()
        messages.success(request, "Your account has been created!")
        return render(request, "signin.html")

    except IntegrityError as e:
        messages.error(request, e)
        return render(request, "signup.html")


def Logout(request):
   logout(request)
   messages.success(request, "You have successfully logged out!")
   return render(request, "signin.html")

def post(request):
    Title = request.POST.get("title")
    Img = request.POST.get("dp11")
    Summary = request.POST.get("sum")
    Categories = request.POST.get("categor").lower()
    Content = request.POST.get("cont")
    author = request.POST.get("author")


    if Summary == "" or Categories == "" or Content == "" or Img == "":
        draft = Draft(Title=Title, Summary=Summary, Categories=Categories, Content=Content, Image=Img, Written_by=author)
        draft.save()
        queries = []
        queryset = Draft.objects.filter(Written_by=author)
        for i in queryset:
            queries.append(i)
        messages.success(request, "Saved as Draft!")
        return render(request, "Drafts.html", {"draft":queries})
    if len(Summary.split(" ")) > 15:
        Sum = ""
        Summary =(Summary.split(" ")[0:15])

        for i in Summary:
            Sum = Sum+str(i)+","
        Sum = Sum.replace(',',' ')
        Sum = Sum+"..."

    else:
        Sum = Summary
        pass

    blog = Blog(Title=Title, Image=Img, Categories=Categories,Summary=Sum,Content=Content, Written_by=author)
    blog.save()
    messages.success(request,"You have posted a blog!")
    user = authenticate(username=signin.U, password=signin.P)
    if user:
        login(request, user)
          
    person = Person.objects.filter(Username=signin.U)
    return render(request, "Doctor.html", {"person": person})
    

def book(request):
    return render(request, "Appointment.html")

def Appoint(request):
    Speciality = request.POST.get("speciality")
    time = request.POST.get("date")
    start = datetime.strptime(time, '%Y-%m-%dT%H:%M')
    end = start + timedelta(minutes=45)
    appoint_obj = Appointment(Speciality=Speciality, date_time=time)
    appoint_obj.save()
    messages.success(request, f"You have booked an appointment! ({start}-{end})")
    user = authenticate(username=signin.U, password=signin.P)
    if user:
        login(request, user)
          
    obj = Blog.objects.filter(Categories = signin.blc)
    pers = Person.objects.filter(Category='doctor')
    if obj:
        pass
    blgs = []
    for i in obj:
        blgs.append(i)
    person = Person.objects.filter(Username=signin.U)
    return render(request, "Patient.html", {"person": person,"blgs":blgs,"pers":pers})

