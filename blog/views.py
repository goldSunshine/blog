#coding:UTF-8
from django.shortcuts import render
from blog.models import Article
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
import datetime

#---------------------博客档案-----------------------------------
def art_document(post_list):
    article_type = []
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
    return dict_document    
#----------------------------------------------------------------


#-------------------博客分类------------------------------------
def art_type(post_list):
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
    return dict_type
#---------------------------------------------------------------



def handle_post(request):
    print "it is a test"
    
    num = request.POST['num']
    id_art = request.POST['id']
    print num
    print id_art
    Article.objects.filter(id=str(id)).update(zan=num)
    return HttpResponse("<h1>test</h1>")


def home(request):
    article_type = []
    post_list = Article.objects.all()
   

#---------------------博客档案-----------------------------------
    dict_document = art_document(post_list)
#----------------------------------------------------------------

#-------------------博客分类------------------------------------
    dict_type = art_type(post_list) 
#---------------------------------------------------------------

    limiate = 10
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
    print post.zan
    post_list = Article.objects.all()
    dict_document = art_document(post_list)
    dict_type = art_type(post_list) 
    return render(request,'post.html',{"post":post,"art_docu":dict_document,"art_type":dict_type})





