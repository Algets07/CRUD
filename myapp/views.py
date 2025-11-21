from django.shortcuts import render,redirect
from django.contrib.auth import login,logout

# Create your views here.
def index(request):
    return render(request, 'index.html')


from .models import movie
from django.core.mail import send_mail
from django.conf import settings

def result(request):
    data = movie.objects.all()
    return render(request, 'result.html',{'data':data})

def delete_id(request,id):
    del_item = movie.objects.get(id=id)
    print(del_item.id)
    del_item.delete()
    return redirect('result')

def update_id(request,id):
    update_item = movie.objects.get(id=id)
    if request.method == 'POST':
        name= request.POST['name']
        desc= request.POST['desc']
        img = request.FILES.get('img')
        if name:
            update_item.name=name
        if desc:
            update_item.desc = desc
        if img:
            update_item.img = img
        update_item.save()
        return redirect('result')
        
    return render(request,'update.html',{'data': update_item})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, 'register.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect("login")

import random

def submit_form(request):
    if request.method == 'POST':

        # STORE form data temporarily in session
        request.session['name'] = request.POST['name']
        request.session['desc'] = request.POST['desc']
        request.session['img'] = request.FILES['img'].name  # store filename only

        # Save image temporarily to session folder
        img_file = request.FILES['img']
        request.session['uploaded_image'] = img_file.name

        # Generate OTP
        otp = random.randint(100000, 999999)
        request.session['otp'] = otp
        request.session.set_expiry(30)

        # Send OTP Email
        send_mail(
            subject="Your OTP Code",
            message=f"Your OTP is {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["algetes2004@gmail.com"],
            fail_silently=False,
        )

        # Store uploaded file in temp folder
        with open("media" + img_file.name, "wb+") as dest:
            for chunk in img_file.chunks():
                dest.write(chunk)

        return redirect('verify_otp')

    return redirect('index')

def verify_otp(request):
    if request.method == "POST":
        user_otp = request.POST['otp']
        session_otp = str(request.session['otp'])

        if user_otp == session_otp:

            # RETRIEVE SAVED DATA
            name = request.session['name']
            desc = request.session['desc']
            img_name = request.session['uploaded_image']

            # Move image from temp to main folder
            from django.core.files import File
            f = open("media" + img_name, "rb")
            
            movie.objects.create(
                name=name,
                desc=desc,
                img=File(f)
            )
            f.close()

            return redirect('result')

        return render(request, "otp.html", {'msg': 'Invalid OTP!'})

    return render(request, 'otp.html')

 
def resend(request):
    import random
    new_otp = random.randint(100000, 999999)
    request.session['otp'] = new_otp
    request.session.set_expiry(30)
    send_mail(
            subject="Your OTP Code",
            message=f"Your OTP is {new_otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["algetes2004@gmail.com"],
            fail_silently=False,
        )
    return redirect('verify_otp')
