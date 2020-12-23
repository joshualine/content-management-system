from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]
