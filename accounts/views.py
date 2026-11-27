from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

class CustomLoginVieW(LoginView):
    template_name = 'accounts/login.html'

def logout_view(request):
    logout(request)
    return redirect ('home')

def home_view(request):
    if not request.user.is_authenticated:
        user_role = 'VISITANTE'
    else:
        user_role = request.user.role

        context ={
            'user_role': user_role
        }
        return render(request, 'home .html', context)