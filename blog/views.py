from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/list_post.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail_view.html'
