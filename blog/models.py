#coding:UTF-8

from django.db import models
from DjangoUeditor.models import UEditorField

class Article(models.Model):
    title = models.CharField("博客标题",max_length = 100)
    category = models.CharField("博客标签",max_length = 50,blank = True)
    pub_date = models.DateTimeField("发布时间",auto_now_add = True,editable=True)
    update_time = models.DateTimeField("跟新时间",auto_now=True,null=True)
    content = UEditorField("文章正文",height=300,width=1000,default="",blank=True,imagePath="uploads/blog/images/",
                           toolbars="besttome",filePath="uploads/blog/files")
    zan = models.IntegerField(default=0)
    read_num = models.IntegerField(default=0)


    def __unicode__(self):
        return self.title

    class Meta():
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"



class Comment(models.Model):
    art_id =  models.IntegerField()
    discuss = models.CharField("评论",max_length = 500)
    comment_time = models.DateTimeField("评论时间",auto_now=True,null=True)

    def __unicode__(self):
        return self.discuss
    
    class Meta():
        ordering = ['-comment_time']

