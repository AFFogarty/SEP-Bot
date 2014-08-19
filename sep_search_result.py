from lxml import html
import re
import requests
from constants import SEP_URL


class SEPSearchResult():

    query = None
    results = None

    def __init__(self, query):
        self.set_query(query)

    def set_query(self, query):
        self.query = str(query).lower().split()

    @property
    def url(self):
        url = SEP_URL + "search/searcher.py?query="
        for word in self.query:
            url += word + "+"
        return url

    def request_results(self):
        page = requests.get(self.url)
        # Remvoe bold tags
        text_no_bold = re.sub('</? ?b>', '', page.text)
        text_no_newlines = re.sub('\n', '', text_no_bold)
        tree = html.fromstring(text_no_newlines)
        titles = tree.xpath("//div[@class='result_title']/a/text()")
        urls = tree.xpath("//div[@class='result_title']/a/@href")
        # Build the output tuples
        output = []
        for i in range(len(titles)):
            output.append(
                {
                    "title": titles[i],
                    "url": SEP_URL + urls[i].lstrip("../")
                }
            )
        self.results = output
        return output