from django.shortcuts import get_object_or_404
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


def get_more_articles(request, fetch_count=10):
    pass


def search(request, query_string, fetch_count=10):
    pass
