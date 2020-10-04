from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator 
from .models import *
# from .forms import CommentForm



def base(request):
   return render(request,'html/base.html')

def blog(request):
    post = MainDiscussion.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(post, 10)
    page_obj = paginator.get_page(page)
    context = {'post': page_obj}
    return render(request, 'html/blog.html', context)

def posting(request, pk):
    post = MainDiscussion.objects.get(pk=pk)
    return render(request, 'html/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        if request.POST['dis_title']:
            new_article=MainDiscussion.objects.create(
                dis_title=request.POST['dis_title'],
                dis_desc=request.POST['dis_desc'],
            )
        else:
            new_article=MainDiscussion.objects.create(
                dis_title=request.POST.get['dis_title'],
                dis_desc=request.POST.get['dis_desc'],                
            )
        return redirect('/blog/')
    return render(request, 'html/new_post.html')

def remove_post(request, pk):
    post = MainDiscussion.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'html/remove_post.html', {'Post': post})

