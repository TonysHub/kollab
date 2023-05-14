from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class HomeView(generic.TemplateView):
    template_name = 'home/home.html'

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'home/signup.html'
    success_url = reverse_lazy('login')
    # if form_class.role == 'Creator':
    #     success_url = reverse_lazy('creator-home')
    # elif form_class.role == 'Business':
    #     success_url = reverse_lazy('business-home')
        

# class LoginView(generic.TemplateView):
#     form_class = LoginForm
#     template_name = 'home/login.html'
#     success_url = reverse_lazy('login')

class LoginView(generic.TemplateView):
    template_name = 'home/login.html'
    form_class = LoginForm
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home:success'))
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(reverse('home:home'))
    
    # Populate form at GET request (start of page)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    
class SuccessView(generic.TemplateView):
    template_name = 'home/success.html'
