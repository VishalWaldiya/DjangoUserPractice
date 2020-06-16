from django.shortcuts import render,reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import Article
from django.db.models import Q

class Dashboard(LoginRequiredMixin,TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        articles = Article.objects.filter(Q(tags__icontains=self.request.user.preferences)|Q(category__icontains=self.request.user.preferences))
        context['object_list'] = articles
        return context
    

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
