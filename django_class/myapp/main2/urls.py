from django.urls import path
from . import views

urlpatterns = [
    path("hi/",  views.welcome),
    path("hey/", views.hello),
    path("come/", views.back),
    path("blogers/", views.war),
    path("social/", views.timzy)
]