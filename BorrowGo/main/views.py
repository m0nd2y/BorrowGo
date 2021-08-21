#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from random import *
from .models import *
from sendEmail.views import *
import hashlib
#finish_project

# Create your views here.
def index(request):
    if 'user_name' in request.session.keys() :
        lists = User.objects.all()
        content = {'lists':lists}
        return render(request, 'postlist.html', content)
    else :
        return redirect('main_signin')

def signup(request):
    return render(request, 'signup.html')

def join(request):
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    name = request.POST['signupName']
    phone = request.POST['signupPhone']
    encoded_pw = pw.encode()
    encrypted_pw = hashlib.sha256(encoded_pw).hexdigest()
    user = User(user_id = name,  user_pw = encrypted_pw, user_email = email, user_phonenumber=phone)
    try :
        user.save()
    except :
        print(":(")
    response = redirect('main_index')
    response.set_cookie('user_id', user.user_id)
    return response

def signin(request):
    return render(request, 'signin.html')

def login(request) :
    loginEmail = request.POST['loginEmail']
    print("loginEmail", loginEmail)
    loginPW = request.POST['loginPW']
    print("loginPW", loginPW)
    try :
        user = User.objects.get(user_email = loginEmail)
    except :
        messages.info(request, 'login fail')
        return HttpResponseRedirect('/signin')
    ##login_pw_enc
    encoded_loginPW = loginPW.encode()
    encrypted_loginPW = hashlib.sha256(encoded_loginPW).hexdigest()
    if user.user_pw == encrypted_loginPW:
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return redirect('main_index')
    else :
        messages.info(request, 'login fail')
        return HttpResponseRedirect('/signin')
    
def loginFail(request) :
    return render(request, 'loginFail.html')

def logout(request) :
    del request.session['user_name']
    del request.session['user_email']
    return redirect('main_signin')

def result(request):
    if 'user_name' in request.session.keys() :
        content = {}
        content['grade_calculate_dic'] = request.session['grade_calculate_dic']
        content['email_domain_dic'] = request.session['email_domain_dic']
        del request.session['grade_calculate_dic']
        del request.session['email_domain_dic']
        return render(request, 'result.html', content)
    else :
        return redirect('main_signin')