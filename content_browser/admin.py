from django.contrib import admin
from .models import Author, Article

admin.site.site_header = "WebNotes Blog"
admin.site.site_title = "WebNotes Blog admin panel"
admin.site.index_title = "Site administration panel"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('header', 'publication_date')

    list_filter = ('publication_date', 'authors')

    date_hierarchy = 'publication_date'

    filter_horizontal = ('authors',)

    search_fields = ['header']
