from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('list_post/', PostListView.as_view(), name='post_list'),
    path('detail_post/<pk>/', PostDetailView.as_view(), name='post_detail'),
]
