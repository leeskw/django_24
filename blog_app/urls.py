from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('article/<slug:slug>/', views.detail , name='detail'),
    # path('create/article/', views.create_article, name='create-article'), 
    # path('update/article/<slug:slug>/', views.update_article, name='update-article'), 
    # path('delete/article/<slug:slug>/', views.delete_article, name='delete-article'), 
    path('create/article/', views.BlogCreateView.as_view(), name='create-article'), 
    path('update/article/<slug:slug>/', views.BlogUpdateView.as_view(), name='update-article'), 
    path('delete/article/<slug:slug>/', views.BlogDeleteView.as_view(), name='delete-article'), 
]
