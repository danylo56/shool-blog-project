from django.http import JsonResponse
from django.shortcuts import render
from .models import Article
from django.views import generic
from .forms import SearchForm
import urllib


def home(request):
    recent_blogs = Article.objects.all().order_by('-pub_date')[:3]
    return render(request, 'articles/home.html', {'recent_blogs': recent_blogs})


def all_blogs(request):
    blogs = Article.objects.all().order_by('-pub_date')
    return render(request, 'articles/all_blogs.html', {'blogs': blogs})


def search(request):
    search_form = SearchForm()
    return render(request, 'articles/search.html', {'search_form': search_form})


def search_blog(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        encoded_search_term = urllib.parse.unquote(search_form.cleaned_data['search_term'])
        print(encoded_search_term)
        results = []
        articles = Article.objects.all()
        for article in articles:
            if encoded_search_term.lower() in article.title.lower() or encoded_search_term.lower() in article.summary().lower():
                json_article_object = {'id':article.id,
                                       'title': article.title,
                                       'text': article.summary(),
                                       'image_url': article.image.url,
                                       'pub_date': article.pub_date_pretty()
                                       }
                results.append(json_article_object)
        return JsonResponse({'results': results})
    else:
        return JsonResponse({'error': 'Not able to validate form'})


class DetailBlog(generic.DetailView):
    model = Article
    template_name = 'articles/detail_blog.html'


