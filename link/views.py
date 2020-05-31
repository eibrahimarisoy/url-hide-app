from django.shortcuts import redirect, render
from .models import Link, ClickCount

from user.forms import RegisterForm, LoginForm


def index(request):
    context = dict()

    return render(request, 'page/index.html', context)