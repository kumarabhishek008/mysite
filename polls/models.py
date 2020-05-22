from django.db import models
from django.utils import timezone
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

@receiver(post_save,sender=Book)
def book_created(sender,instance,created,**kwargs):
    if created:
        #Book.objects.create(title=instance.title,publication_date=instance.publication_date)
        print("new book published" , Book.title)

@receiver(pre_save,sender=Book)
def book_updated(sender,instance,raw,**kwargs):

    if raw==True:
        #instance.save()
        print("book updated")
    else:
        print("book is not updated")