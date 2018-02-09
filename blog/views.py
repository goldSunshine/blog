from django.shortcuts import render
from blog.models import Article
from django.http import HttpResponse
import datetime

def Test(request):
    post = Article.objects.all()
    #return HttpResponse(post[0].content+post[0].title+post[0].category)
    return render(request,'test.html',{'current_time':datetime.datetime.now()})


def home(request):
    post_list = Article.objects.all()

    return render(request,'home.html',{'post_list':post_list})


def detail(request,id):
	post = Article.objects.get(id = str(id))
	return render(request,'post.html',{"post":post})
