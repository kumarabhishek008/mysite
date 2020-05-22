from django.views.generic import ListView,DetailView
from .models import *
from django.db.models.signals import post_save
from django.db.models import signals
class PublisherList(ListView):
    model = Book
    #publisher = Publisher.objects.all()
    template_name = 'polls/index.html'
    context_object_name = 'book'

class PublisherDetail(DetailView):
    model = Book
    template_name = 'polls/detail.html'
    context_object_name = 'book'







