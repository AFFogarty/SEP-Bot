from lxml import html
import re
import requests
from sep_search.models import Article, Author


class ArticleContentScraper():
    url = None
    article_model = None

    def __init__(self, url):
        """
        Construct the article scraper for the article with the given URL

        :param url:
        :return:
        """
        self.url = url
        self.article_model = Article()

    def scrape(self):
        """
        Scrape the web content from the url.
        :return:
        """
        page = requests.get(self.url)
        # Remvoe bold tags
        # text_no_bold = re.sub('</? ?b>', '', page.text)
        # text_no_newlines = re.sub('\n', '', text_no_bold)
        tree = html.fromstring(re.sub('\n', ' ', page.text).encode('utf-8'))
        # Article title from the SEP
        self.article_model.url = self.url
        self.article_model.title = tree.xpath('//*[@id="aueditable"]/h1/text()')[0]
        self.article_model.summary = tree.xpath('//*[@id="preamble"]/p/text()')[0]
        self.article_model.headings = tree.xpath('//*[@id="toc"]/ul/li/text()')
        self.article_model.content = tree.xpath('//*[@id="main-text"]/p/text()')
        # Handle the author
        author_names = tree.xpath('//*[@id="article-copyright"]/p/a[2]/text()')[0].split()
        author = Author()
        # Pop off the first name
        author.first_name = author_names.pop(0)
        # Merge the rest of names and make it the last name and save the author
        author.last_name = ' '.join(author_names)
        author.save()
        self.article_model.author = author


    def save_article(self):
        """
        Save the article model to the database.
        :return:
        """
        self.article_model.save()