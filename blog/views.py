from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date
from .models import Author, Post, Tag



def starting_page(request):
    latest_post = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
                  'posts': latest_post})


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {
                  'posts': all_posts})


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
                  'post': post,
                    'post_tags': post.tags.all(),
                    })