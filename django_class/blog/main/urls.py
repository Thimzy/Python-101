from django.urls import path
from . import views

urlpatterns = [
    path("headers/", views.home_page, name="homepage"),
    path("abouts/", views.about_page, name="aboutpage")
]