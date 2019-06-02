from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
class ModelView(TemplateView):
    template_name = "main/index.html"
