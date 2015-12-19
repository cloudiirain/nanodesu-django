from django.shortcuts import render, get_object_or_404
from nanodesu.models import Series, Post

def index(request):
    series_list = Series.objects.all()
    context = { 'series_list' : series_list }
    return render(request, 'nanodesu/index.html', context)

def view_series(request, slug):
    series = get_object_or_404(Series, slug=slug)
    context = { 'series' : series }
    return render(request, 'nanodesu/series_detail.html', context)

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = { 'post' : post }
    return render(request, 'nanodesu/post_detail.html', context)