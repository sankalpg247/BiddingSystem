from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm


# Create your views here.
def register(Request):
    msg = None
    if Request.method == 'POST':
        form = SignUpForm(Request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('/login')
        else:
            msg = 'form is not valid'
    else:
        msg = ''
        form = SignUpForm()
    return render(Request, 'registration/register.html', {'form': form, 'msg': msg})


def login_view(Request):
    form = LoginForm(Request.POST or None)
    msg = None
    if Request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(Request, user)
            return redirect('Home')

        else:
            msg = 'error validating form'
    return render(Request, 'registration/login.html', {'form': form, 'msg': msg})


def logout_view(Request):
    logout(Request)
    return redirect('/login')
