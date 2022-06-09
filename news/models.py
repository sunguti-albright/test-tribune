from distutils.command.upload import upload
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# from cloudinary.models import Cloudinary

# Create your models here.
class tags(models.Model):
    name  = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'tags'
    
# one to many relationship
class Article(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags)
    article_image = models.ImageField(upload_to = 'articles/', blank=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_article(self):
        self.save()
        
    #method that queries the database and returns the results
    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
    
    @classmethod
    def today_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news    

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Articles'
    
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    
    class Meta:
        verbose_name_plural = 'News Letter Recipients'
    
    def __str__(self):
        return self.name
