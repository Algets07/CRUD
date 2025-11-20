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
    if request.method == 'POST':
        name= request.POST['name']
        desc= request.POST['desc']
        img = request.FILES['img']
        movie.objects.create(name=name,desc=desc,img=img)
        send_mail(
    subject="New Student Form Submitted",
    message=f"Name: {name}\nDesc: {desc}\nForm submitted successfully!",
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=["algetes2004@gmail.com"],
    fail_silently=False
)

        return redirect('result')
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
 
