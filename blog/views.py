from django.shortcuts import render
from blog.models import Article
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
import datetime

def test(request):
    post = Article.objects.all()
    #return HttpResponse(post[0].content+post[0].title+post[0].category)
    return render(request,'1.html')


def home(request):
    post_list = Article.objects.all()
    limiate = 5
    paginator = Paginator(post_list,limiate)

    page = request.GET.get('page')
    
    try:
        post_list_page = paginator.page(page)
    except PageNotAnInteger:
        post_list_page = paginator.page(1)
    except EmptyPage:
        post_list_page = paginator.page(paginator.num_pages)
     
    return render(request,'a.html',{'post_list':post_list_page})


def detail(request,id):
	post = Article.objects.get(id = str(id))
	return render(request,'post.html',{"post":post})
