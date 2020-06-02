from django.urls import path
from .views import hide_link_create, user_link_info, link_delete

urlpatterns = [
    path('hide-link-create/', hide_link_create, name="hide_link_create"),
    path('user-link-info/', user_link_info, name="user_link_info"),
    path('link-delete/<int:id>/', link_delete, name="link_delete"),
]
