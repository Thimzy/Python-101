from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="homepage"),
    path("about/", views.about_page, name="aboutpage"),
    path("about/", views.about_page, name="aboutpage"), 
    path("about/<int:name>/boys/<int:age>", views.about_pages)
]
    