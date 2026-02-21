from django.urls import path
from . import views


urlpatterns = [
    path("", views.MenuListView.as_view(), name="home"),
    path("", views.MenuItemDetailView.as_view(), name="index"),
]
