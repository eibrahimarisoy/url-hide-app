from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from user.forms import LoginForm, RegisterForm


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
    return render(request, "page/user_register.html", context)


def user_login(request):
    context = dict()
    form = LoginForm(request.POST or None)
    context["login_form"] = form
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        # if username is not exists throw and error to user
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            messages.info(request, "Kullanıcı adı yanlış.")
            return render(request, "page/user_login.html", context)

        # check username and password are correct
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, "Kullanıcı adı veya parola yanlış.")
            return render(request, "page/user_login.html", context)
        else:
            messages.success(request, "Başarıyla giriş yaptınız.")
            # start new session for user
            login(request, user)
            return redirect("index")

    return render(request, "page/user_login.html", context)


@login_required
def user_logout(request):
    logout(request)
    return redirect("index")


@login_required
def user_change_password(request):
    context = dict()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Parolanız başarıyla değiştirildi.')
            return redirect('user_link_info')
        else:
            messages.error(request, 'Lütfen parolanızı doğru giriniz.')
    else:
        form = PasswordChangeForm(request.user)

    context['form'] = form
    return render(request, 'page/user_password_change.html', context)
