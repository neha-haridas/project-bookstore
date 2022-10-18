
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User, auth, models
from .models import User
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['email']
        phonenumber = request.POST.get('phonenumber')
        hname=request.POST['hname']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        password = request.POST.get('password')

        if password == cpassword:
            if User.objects.filter(email=email).exists():

                # print('5')
                messages.info(request, 'email already taken')
                return render('register/')
            else:
                user = User.objects.create_user(username=username, first_name=first_name,
                                                last_name=last_name, email=email,
                                                phonenumber=phonenumber,hname=hname,country=country, state=state,
                                                city=city, pincode=pincode, password=password)

                user.save()

                # login = tbl_userLogin(username=username, password=password)
                # login.save()
                return redirect('login')
        else:
            print('password is not matching')
            return redirect('reg base.html')
    else:
        return render(request, 'reg base.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = auth.authenticate(email=email, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            # save email in session
            request.session['email'] = email
            if user.is_admin:
                return redirect('admin/')

            else:
                return redirect('/')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/login/login/login/register/')
    return render(request, 'login.html')


# @login_required
def changepassword(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)
        if success:
            user.set_password(new_password)
            user.save()
            messages.info(request, 'Password updated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('changepassword')
    return render(request, 'changepassword.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
