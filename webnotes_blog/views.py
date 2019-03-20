from django.shortcuts import render
from content_browser.models import Article


def home_page(request):
    last_10_articles = Article.objects.all()[:10]
    return render(request, 'index.html', {'last_10_articles': last_10_articles})
