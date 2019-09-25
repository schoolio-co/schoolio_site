import random
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView, FormView


dt = datetime.datetime.now()
 

class landing(TemplateView):
    template_name = 'index.html'

class blog(TemplateView):
    template_name = 'blog.html'

def error_404(request, exception):
        data = {}
        return render(request,'error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'error_500.html', data)