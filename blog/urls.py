from django.urls import path
from .views import (
	Dashboard,ArticleCreateView,ArticleDeleteView,ArticleListView,
ArticleDetailView,ArticleUpdateView)

urlpatterns = [
	path('', Dashboard.as_view() , name="home"),
    path('article-create/',ArticleCreateView.as_view() , name="create-Article"),
    path('article-delete/<int:pk>/', ArticleDeleteView.as_view() , name="delete-Article"),
    path('article-list/', ArticleListView.as_view() , name="list-Article"),
    path('article-detail/<int:pk>/', ArticleDetailView.as_view() , name="detail-Article"),
    path('article-update/<int:pk>/', ArticleUpdateView.as_view() , name="update-Article"),
]