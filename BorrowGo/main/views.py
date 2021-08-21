from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from random import *
from .models import *
from sendEmail.views import *
import hashlib
#finish_project

# Create your views here.
def index(request):
    if 'user_name' in request.session.keys() :
        return render(request, 'index.html')
    else :
        return redirect('main_signin')

def signup(request):
    return render(request, 'signup.html')

def join(request):
    name = request.POST['signupName'].encode('utf-8').decode('iso-8859-1')
    email = request.POST['signupEmail'].encode('utf-8').decode('iso-8859-1')
    pw = request.POST['signupPW']
    encoded_pw = pw.encode()
    encrypted_pw = hashlib.sha256(encoded_pw).hexdigest()
    user = User(user_id = name,  user_pw = encrypted_pw, user_email = email)
    user.save()
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
        return redirect('main_loginFail')
    ##login_pw_enc
    encoded_loginPW = loginPW.encode()
    encrypted_loginPW = hashlib.sha256(encoded_loginPW).hexdigest()
    if user.user_pw == encrypted_loginPW:
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return redirect('main_index')
    else :
        return redirect('main_loginFail')
    
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