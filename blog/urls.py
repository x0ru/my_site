from django.urls import path
from . import views


urlpatterns = [
    path('', views.starting_page, name='starting_page_page'),
    path('posts', views.posts, name='posts_page'),
    path('posts/<slug:slug>', views.post_details, name='post_details_page'),
]


