#coding:UTF-8

from django.db import models
from DjangoUeditor.models import UEditorField

class Article(models.Model):
    title = models.CharField("博客标题",max_length = 100)
    category = models.CharField("博客标签",max_length = 50,blank = True)
    pub_date = models.DateTimeField("发布时间",auto_now_add = True,editable=True)
    update_time = models.DateTimeField("跟新时间",auto_now=True,null=True)
    #content = models.TextField(blank=True,null=True)

    content = UEditorField("文章正文",height=300,width=1000,default="",blank=True,imagePath="uploads/blog/images/",
                           toolbars="besttome",filePath="uploads/blog/files")


    def __unicode__(self):
        return self.title

    class Meta():
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"
