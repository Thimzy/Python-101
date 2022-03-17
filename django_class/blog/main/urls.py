from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
 # post views
    path('', views.post_list, name='post_list'),
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>/',views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',
 views.post_share, name='post_share')
]