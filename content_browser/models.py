import random

from django.contrib.auth.models import User as UserModel
from django.db import models
from django.utils import timezone
from django.utils.lorem_ipsum import paragraphs as lorem_ipsum_paragraphs


class Author(UserModel):

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


def generate_random_article_content():
    return '\n\n'.join(lorem_ipsum_paragraphs(random.randint(10, 20),
                                              common=False))


class Article(models.Model):
    header = models.CharField(max_length=150,
                              unique_for_date="publication_date")
    content = models.TextField(default=generate_random_article_content)
    publication_date = models.DateTimeField(default=timezone.now)
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.header
