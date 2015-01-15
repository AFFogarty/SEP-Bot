
from django.core.management.base import BaseCommand
from django.core.management import call_command
from sep_search.scraper.article_content_scraper import ArticleContentScraper


class Command(BaseCommand):
    args = ""

    def handle(self, *args, **kwargs):
        url_list = [
            "http://plato.stanford.edu/entries/plato/",
            "http://plato.stanford.edu/entries/aesthetic-concept/"
        ]
        for url in url_list:
            scraper = ArticleContentScraper(url)
            scraper.scrape()
            scraper.save_article()
