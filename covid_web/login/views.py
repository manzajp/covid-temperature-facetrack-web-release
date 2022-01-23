from pyexpat import model
from urllib import request
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, ListView

from .models import User
from camera.models import Camera

class LandingView(TemplateView):
    template_name = "login/landing.html"

class AboutUsView(TemplateView):
    template_name = "login/aboutus.html"

class RegisterView(TemplateView):
    template_name = "login/register.html"

def register(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        oldUser = User.objects.get(userName=request.POST['username'])

    except(User.DoesNotExist):
        newUser = User(userName=username, email = email, password = password, date = timezone.now())
        newUser.save()
        # should be success page
        return redirect('login:login')

    else:
        response = "User existed."
        return HttpResponse(response)

class LoginView(TemplateView):
    template_name = 'login/login.html'

# login data to dashboard
def auth(request):
    try:
        username = request.POST['username']
        user = User.objects.get(userName=username)
    except (User.DoesNotExist):
        response = "User does not exists."
        return HttpResponse(response)
    else:
        if user.allowed == True:
            if user.password == request.POST['password']:
                request.session['username'] = username
                request.session['email'] = user.email
                return redirect('login:dashboard')
            else:
                response = "Password incorrect."
                return HttpResponse(response)
        else:
            response = "Registration not approved by admin. Please wait at least 1 day or contact the admin if urgent."
            return HttpResponse(response)

class DashboardView(ListView):
    model = Camera
    context_object_name = 'camera_list'
    template_name = 'login/dashboard.html'

    def get_queryset(self):
        user = User.objects.get(userName=self.request.session['username'])
        queryset = Camera.objects.all()
        # queryset = queryset.filter(owner=user)
        return queryset

class AccountView(TemplateView):
    template_name = "login/account.html"

def acc_change(request):
    username = request.session['username']
    password = request.POST['password']
    user = User.objects.get(userName=username)
    user.password = password
    user.save()

    return redirect('login:dashboard')
    
class LogoutView(TemplateView):
    template_name = "login/logout.html"

def logout_control(request):
    request.session.flush()
    return redirect('login:landing')
