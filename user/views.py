from django.shortcuts import redirect, render
from user.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def user_register(request):
    context = dict()
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        # get new user information from form
        username = form.clean_username()
        email = form.clean_email()
        password = form.clean_password()
        # create new user and set_password and set active
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.is_active = True
        new_user.save()
        # login new user
        login(request, new_user)
        messages.success(request, "Başarıyla Kayıt Oldunuz.")
        return redirect("index")

    context["register_form"] = form
    context['login_form'] = LoginForm()
    return render(request, "page/index.html", context)


def user_login(request):
    context = dict()
    form = LoginForm(request.POST or None)
    context["login_form"] = form
    context['register_form'] = RegisterForm()
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        # if username is not exists throw and error to user
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            messages.info(request, "Kullanıcı adı yanlış.")
            return render(request, "page/index.html", context)

        # check username and password are correct
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, "Kullanıcı adı veya parola yanlış.")
            return render(request, "page/index.html", context)
        else:
            messages.success(request, "Başarıyla giriş yaptınız.")
            # start new session for user
            login(request, user)
            return redirect("index")

    return render(request, "page/index.html", context) 