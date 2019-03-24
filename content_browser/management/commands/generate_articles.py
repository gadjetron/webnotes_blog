import random

from django.core.management import BaseCommand, CommandError
from content_browser.models import Article, Author


class Command(BaseCommand):
    help = """\
        Generate random articles in amount specified by <count> parameter
        """

    def add_arguments(self, parser):
        parser.add_argument('count',
                            type=int,
                            help='How many articles to generate')

    def handle(self, *args, **options):
        stdwrite = self.stdout.write
        success_msg = '{} article(-s) was successfully generated!'

        if options['count'] <= 0:
            raise CommandError("'count' parameter must be greater than 0!")
        else:
            articles_exists = Article.objects.exists()

            authors = Author.objects.all()
            authors_exists = authors.exists()
            authors_count = authors.count()

            if not authors_exists:
                raise CommandError(
                    "Create 1 or more authors in admin interface!")
            else:
                # Runs if 'Articles' table is empty.
                if not articles_exists:
                    if authors_count == 1:
                        article_author = authors[0]

                        for i in range(1, options['count'] + 1):
                            article_header = "Article %s" % str(i)

                            article = Article.objects.create(header=article_header)
                            article.authors.set([article_author])

                        stdwrite(self.style.SUCCESS(
                            success_msg.format(options['count'])))
                    else:
                        for i in range(1, options['count'] + 1):
                            article_header = "Article %s" % str(i)
                            article_author = random.choice(authors)

                            article = Article.objects.create(header=article_header)
                            article.authors.set([article_author])

                        stdwrite(self.style.SUCCESS(
                            success_msg.format(options['count'])))
                else:
                    if authors_count == 1:
                        article_author = authors[0]

                        for i in range(options['count']):
                            last_article_id = Article.objects.last().id
                            article_header = "Article %s" % str(last_article_id + 1)

                            article = Article.objects.create(header=article_header)
                            article.authors.set([article_author])

                        stdwrite(self.style.SUCCESS(
                            success_msg.format(options['count'])))
                    else:
                        for i in range(options['count']):
                            last_article_id = Article.objects.last().id
                            article_header = "Article %s" % str(last_article_id + 1)
                            article_author = random.choice(authors)

                            article = Article.objects.create(header=article_header)
                            article.authors.set([article_author])

                        stdwrite(self.style.SUCCESS(
                            success_msg.format(options['count'])))
