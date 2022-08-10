from django.shortcuts import render
from django.views.generic import ListView
from . models import message
class home_page_view(ListView):
    model= message
    template_name='home.html'
    'note listview returns an object called object_list'
    'for explicity lets create content_object_name instead of object_list'
    context_object_name='all_content'

# Create your views here.
