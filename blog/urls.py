from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView

urlpatterns = [
    path('' , BlogListView.as_view() , name='home'),
    path('post/<slug:slug>/' , BlogDetailView.as_view() , name='detail'),
    path('new/', BlogCreateView.as_view(), name='post_new'),
] 