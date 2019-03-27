from django.urls import re_path
from . import views as cb_views


urlpatterns = [
    re_path(r'^article/(?P<id>\d+)$', cb_views.get_article_content,
            name="article"),
    re_path(r'^articles/load_more$', cb_views.get_more_articles,
            name="load_more_articles"),

    re_path(r'^search$', cb_views.search, name="search"),
    re_path(r'^search/load_more$', cb_views.search_more,
            name="load_more_search_results")
]

content_browser_urlpatterns = urlpatterns
