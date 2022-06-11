
from email.policy import default
from django.db import models
import datetime as dt
from django.contrib.auth.models import User

class tags(models.Model): #details about different tags contained in an Article.
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()   

from tinymce.models import HTMLField
class Article(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null = True,)  #store the ID of the Editor from the Editor table.
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True) #get the dates when articles were posted we need to add a timestamp .. DateTimeField to store the exact date and time our article was posted... auto_now_add and equate it to True. This will automatically save the exact time and date 
    article_image = models.ImageField(upload_to = 'articles/', default='IMAGE') #add a new field to our database
    
    def __str__(self):
        return self.title  #show title instead of article (1) in the admin part
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    #method that will query the database and fetch our results.
    @classmethod
    def search_by_title(cls,search_term): # filter the all the Articles in our database and return ones matching to our search query
        news = cls.objects.filter(title__icontains=search_term) # __icontains query filter check if any word in the titlefield of our articles matches the search_term.
        return news

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)