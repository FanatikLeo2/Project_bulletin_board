from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Reply
from .forms import PostCreateForm, ReplyCreateForm


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    model = Post
    template_name = 'post_createform.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostCreateForm
    model = Post
    template_name = 'post_createform.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_deleteform.html'
    success_url = reverse_lazy('post_list')


class ReplyCreate(LoginRequiredMixin, CreateView):
    form_class = ReplyCreateForm
    model = Reply
    template_name = 'reply_createform.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=int(self.kwargs['pk']))
        return super().form_valid(form)


class ReplyList(ListView):
    model = Reply
    template_name = 'replyes.html'
    context_object_name = 'replyes'


def confirm_reply(request, pk):
    reply = Reply.objects.get(id=pk)
    reply.status = "1"
    reply.save()
    return redirect('reply_list')


def reject_reply(request, pk):
    reply = Reply.objects.get(id=pk)
    reply.status = "2"
    reply.save()
    return redirect('reply_list')


def index(requests):
    posts = Post.objects.all()
    reply = Reply.objects.all()
    return render(requests, 'index.html', context={'posts': posts, 'reply': reply})
