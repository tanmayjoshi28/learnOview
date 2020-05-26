from django.shortcuts import render
from .models import Categories, Video
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def homePage(request):
    all_category = Categories.objects.all()
    all_videos = Video.objects.all()

    context = {'categories': all_category,
               'videos': all_videos}
    return render(request, 'videoCategories/index.html', context)




