from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput)
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    email = forms.EmailField(label="Email", widget=forms.EmailInput)
    password = forms.CharField(
        max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(
        max_length=20, label="Parola Doğrula", widget=forms.PasswordInput)

    def clean(self):
        errors = dict()
        password = self.cleaned_data['password']
        confirm = self.cleaned_data['confirm']
        username = self.cleaned_data['username']
        try:
            email = self.cleaned_data['email'].lower()
        except KeyError:
            raise forms.ValidationError(errors)
        if User.objects.filter(email=email):
            errors['email'] = f"{email} email kullanımda."

        if User.objects.filter(username=username):
            errors['username'] = f"{username} kullanıcı adı kullanımda."

        if len(password) < 8:
            errors['password'] = 'Parolanız en az 8 karakter olmalıdır.'
            errors['confirm'] = 'Parolanız en az 8 karakter olmalıdır.'
        if password != confirm:
            errors['confirm'] = 'Parolanız Eşleşmiyor.'
        if errors:
            raise forms.ValidationError(errors)
    
    def clean_username(self):
        data = self.cleaned_data['username']
        return data

    def clean_email(self):
        data = self.cleaned_data["email"]
        return data.lower()

    def clean_password(self):
        data = self.cleaned_data["password"]
        return data