from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib import messages
class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        messages.success(self.request, "Login successful")
        return reverse_lazy('home')
    
def user_logout(request):
    logout(request)
    return redirect('home')