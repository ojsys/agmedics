from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, View
from django.shortcuts import redirect, render
from .forms import *
from .models import User
from django.conf import settings
from django.contrib import messages



def logout_user(request):
    logout(request)
    return redirect('login')


def signup(request):
    form = UserCreationForm()
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login User
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        
    return render(request, 'account/sign-up.html', {'form': form})


class LoginPageView(View):
    template_name = 'account/sign-in.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, {'message': message, 'form': form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}, You are logged in successfully.'
                return redirect('home')
        message = 'Login failed'    
        return render(request, 'account/sign-in.html', {'form': form, 'message': message})