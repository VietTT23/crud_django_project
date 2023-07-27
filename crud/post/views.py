from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import CreatePostForm
from django.contrib.messages import views
from  django.urls import reverse


# Create your views here.
class ListPostView(generic.ListView):
    model = Post
    template_name = 'post/list_post.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CreatePostView(views.SuccessMessageMixin, generic.CreateView):
    template_name = 'post/create_post.html'
    form_class = CreatePostForm
    success_message = 'CREATE Successfully!'


class UpdatePostView(views.SuccessMessageMixin, generic.UpdateView):
    template_name = 'post/update_post.html'
    model = Post
    fields = ['name', 'content', ]
    success_message = 'UPDATE Successfully!'

    def get_success_url(self):
        return reverse('post:list_post_view', kwargs={})


def delete_post(request, pk):
    post = Post.objects.filter(id=pk)
    post.delete()
    context = {
      "messages": "DELETE successfully",
      'posts': Post.objects.all()
    }
    return render(request, 'post/list_post.html', context)
