from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Article


def get_article_content(request, id):
    try:
        article = get_object_or_404(Article, id=id)
        article_html_string = loader.render_to_string(
            'content_browser/full_article.html',
            context={'article': article}
        )
    except Article.DoesNotExist:
        raise Http404("No such article!")

    return HttpResponse(article_html_string)


def get_more_articles(request):
    fetch_count = int(request.GET['fetch_count'])
    loaded_articles_count = int(request.GET['loaded_articles_count'])

    articles = Article.objects.all()[loaded_articles_count:
                                     loaded_articles_count + fetch_count]

    return render(request, 'content_browser/articles_batch_response.html',
                  {'articles': articles})


def search(request):
    query_string = request.GET['query_string']
    fetch_count = int(request.GET['fetch_count'])

    search_results = Article.objects.filter(header__icontains=query_string)[:fetch_count]

    return render(request, 'content_browser/articles_batch_response.html',
                  {'articles': search_results})
