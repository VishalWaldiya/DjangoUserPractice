from django.shortcuts import render,reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from articles.models import Article


class Dashboard(TemplateView):
    template_name = "home.html"

class ArticleCreateView(CreateView):
    model = Article
    fields = '__all__'
    success_url = '/'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name_suffix='_delete'
    success_url = '/'

class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article

class ArticleUpdateView(UpdateView):
    model = Article
    success_url = '/'
    fields = '__all__'
