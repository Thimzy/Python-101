from django.urls import path
from . import views

urlpatterns = [
    path("home/",  views.welcome),
    path("about/", views.hello),
    path("contacts/", views.back),
    path("blogs/", views.war),
    path("me/", views.timzy)
]
