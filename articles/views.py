from django.shortcuts import render,reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView

from .forms import ArticleForm
from .models import Article

class Dashboard(TemplateView):
    template_name = "home.html"

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/'

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleCreateView, self).get_context_data(**kwargs)
    #     return context
    