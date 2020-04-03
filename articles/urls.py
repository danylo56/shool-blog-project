from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('search', views.search, name='search'),
    path('<int:pk>', views.DetailBlog.as_view(), name='detail'),
    path('search_blog', views.search_blog, name='search_blog')

]