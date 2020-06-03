from django.urls import path

from .views import user_change_password, user_login, user_logout, user_register

urlpatterns = [
    path('user-register/', user_register, name='user_register'),
    path('user-login/', user_login, name="user_login"),
    path('user-logout/', user_logout, name="user_logout"),
    path(
        'user-change-password/',
        user_change_password,
        name="user_change_password"
    ),
]
