#coding:UTF-8
from django.shortcuts import render
from blog.models import Article
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
import datetime

dict_document = {}
dict_type={}
def test(request):
    post = Article.objects.all()
    #return HttpResponse(post[0].content+post[0].title+post[0].category)
    return render(request,'1.html')


def home(request):
    article_type = []
    post_list = Article.objects.all()
    print post_list


#---------------------博客档案-----------------------------------
    for post in post_list:
        time = str(post.pub_date)
        temp = time.split()
        b = temp[0].split("-") 
        article_type.append(b[0]+"-"+b[1])
    a = set(article_type)

    c = []
    num=[0,0,0,0,0]
    count=0
    for x in a:
        num[count] = 0
        for i in article_type:
            if i == x:
                num[count] = num[count] + 1
        c.append((x,num[count]))
        count = count + 1
    dict_document = dict(c)
#----------------------------------------------------------------

#-------------------博客分类------------------------------------
    type_list = [] 
    for post in post_list:
        type_docu = post.category
        type_list.append(type_docu)
    a_type = set(type_list) 
    art_type = []
    num_type=[0,0,0,0,0,0,0,0,0,0,0,0]
    count_type=0
    for x in a_type:
        for i in type_list:
            if i == x:
                num_type[count_type] = num_type[count_type] + 1
        art_type.append((x,num_type[count_type]))
        count_type = count_type + 1
    dict_type = dict(art_type)
    print dict_type
        
#---------------------------------------------------------------

    limiate = 5
    paginator = Paginator(post_list,limiate)

    page = request.GET.get('page')
    
    try:
        post_list_page = paginator.page(page)
    except PageNotAnInteger:
        post_list_page = paginator.page(1)
    except EmptyPage:
        post_list_page = paginator.page(paginator.num_pages)
     
    return render(request,'a.html',{'post_list':post_list_page,"art_docu":dict_document,"art_type":dict_type})


def detail(request,id):
	post = Article.objects.get(id = str(id))
	return render(request,'post.html',{"post":post,"art_docu":dict_document,"art_type":dict_type})
