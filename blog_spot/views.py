from django.shortcuts import render, redirect
from .models import User, Blogs
from django.contrib import messages
from django.http import HttpResponse

def home(req):
    return render(req, 'blog_spot/home.html')
def signup(req):
    if 'submit' in req.POST:
        user_name = req.POST['username']
        password = req.POST['password']
        s = User.objects.filter(usr_name = user_name).exists()
        if not s:
            usr = User()
            usr.usr_name = req.POST['username']
            usr.password = req.POST['password']
            usr.role = 'r'
            usr.save()
        else:
            messages.error(req, 'User name already exists')
    return render(req, 'blog_spot/signup.html')
def blogger_signup(req,usr):
    if 'submit' in req.POST:
        username = req.POST['username']
        if username:
            user = User.objects.filter(usr_name = username).first()
            user.role = 'b'
            user.save()
    return render(req, 'blog_spot/blogger_signup.html',{'user':usr})
def signin(req):
    if 'log' in req.POST:
        usr = User.objects.filter(usr_name = req.POST['username'], password = req.POST['password']).first()
        # print(usr.usr_name)
        if usr:
            return redirect(view_page, usr = usr.usr_name)
        else:
            messages.error(req, "Invalid username or password.")
    return render(req, 'blog_spot/signin.html')
def user_page(req, usr):
    if 'submit' in req.POST:
        pst = req.POST['pst']
        blg = Blogs()
        blg.usr_name = usr
        blg.pst = pst
        blg.save()
    blg = Blogs.objects.filter(usr_name=usr)
    return render(req, 'blog_spot/user_page.html', {'Username':usr, 'blogs':blg})
def view_page(req,usr):
    blg = Blogs.objects.all()
    user = User.objects.filter(usr_name = usr).first()
    return render(req, 'blog_spot/view_page.html',{'Username':user.usr_name, 'blogs':blg, 'status':user.role})