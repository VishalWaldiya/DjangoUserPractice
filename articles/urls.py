from django.urls import path
from .views import Dashboard,ArticleCreateView

urlpatterns = [
    path('', Dashboard.as_view(), name="home"),
    path('article-create', ArticleCreateView.as_view(), name="article-create"),

]