from django.shortcuts import render
from django.views.generic import  TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
class ResumePageView(TemplateView):
    template_name = 'resume.html'
class ServesPageView(TemplateView):
    template_name = 'serves.html'