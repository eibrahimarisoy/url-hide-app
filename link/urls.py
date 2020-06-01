from django.urls import path
from .views import index, hide_link_create, user_link_info, link_forward

urlpatterns = [
    path('index/', index, name='index'),

    path('hide-link-create/', hide_link_create, name="hide_link_create"),
    path('user-link-info/', user_link_info, name="user_link_info"),
]
