from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm, UpdateUserForm, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


def index(request):
    products = Product.objects.filter(is_sale=True)
    return render(request, 'index.html', locals())


def category(request, foo):
    foo = foo.replace("-", " ")
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', locals())
    except:
        messages.success(request, 'این دسته بندی وجود ندارد')
        return redirect('home')


def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', locals())


def sale_products(request):
    products = Product.objects.filter(is_sale=True)
    return render(request, 'sale_products.html', locals())

def search(request):
    query = request.GET['search']
    products = Product.objects.filter(Q(name__icontains=query))
    if not products:
        messages.warning(request, 'محصول مورد نظر یافت نشد. لطفا دوباره امتحان کنید.')
        return redirect('home')
    else:
        return render(request, 'search.html', locals())


def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید.')
            return redirect('home')
        else:
            messages.error(request, 'مشکلی در ورود به صفحه کاربری وجود دارد! لطفاِ دوباره امتحان کنید.')
            return redirect('login')
    else:
        return render(request, 'login.html', locals())


def logout_user(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید.')
    return redirect('login')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'ثبت نام با موفقیت انجام شد. به صفحه کاربری وارد شدید.')
            return redirect('home')
        else:
            messages.success(request, 'مشکلی در ثبت نام وجود دارد! لطفا دوباره امتحان کنید.')
            return redirect('register')
    else:
        return render(request, 'register.html', locals())


def update_user(request):
    if request.user.is_authenticated:
        current_users = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_users)

        if user_form.is_valid():
            user_form.save()

            login(request, current_users)
            messages.success(request, 'اطلاعات بروزرسانی شد.')
            return redirect('update_user')
        return render(request, 'update_user.html', locals())
    else:
        messages.success(request, 'برای دسترسی به صفحه موردنظر ابتدا وارد صفحه کاربری خود شوید.')
        return redirect('home')


def change_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'رمز عبور شما با موفقیت تغییر یافت.')
                login(request, current_user)
                return redirect('update_user')
            else:
                messages.warning(request, 'اطلاعات وارد شده اشتباه است. لطفا دوباره امتحان کنید.')
                return redirect('change_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'change_password.html', locals())
    else:
        messages.success(request, 'برای دسترسی به صفحه موردنظر ابتدا وارد صفحه کاربری خود شوید.')
        return redirect('home')
