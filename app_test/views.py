from django.shortcuts import render
from django.views.generic import ListView
from .models import Default

# Create your views here.

class DefaultListView(ListView):
    model = Default
    template_name = "default/default_list.html"