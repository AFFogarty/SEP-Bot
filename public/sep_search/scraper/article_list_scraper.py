from lxml import html
import re
import requests

SEP_URL = "http://plato.stanford.edu/"

class ArticleListScraper():
    query = None
    results = None

    def __init__(self, query):
        self.set_query(query)

    def set_query(self, query):
        # query_no_accents = remove_accents(query)
        query_no_posessives = re.sub("'s", '', query)
        pattern = re.compile('[^a-zA-Z\d\s]')
        stripped_query = re.sub(pattern, ' ', query_no_posessives)
        # stop_word_filter = StopWordFilter()
        # self.query = stop_word_filter.filter(str(stripped_query).lower().split())

    @property
    def url(self):
        url = SEP_URL + "search/searcher.py?query="
        for word in self.query:
            url += word + "+"
        print url
        return url

    def request_results(self):
        page = requests.get(self.url)
        # Remvoe bold tags
        text_no_bold = re.sub('</? ?b>', '', page.text)
        text_no_newlines = re.sub('\n', '', text_no_bold)
        tree = html.fromstring(text_no_newlines.encode('utf-8'))
        titles = tree.xpath("//div[@class='result_title']/a/text()")
        urls = tree.xpath("//div[@class='result_title']/a/@href")
        # Figure out how many results to return
        result_length = 0
        if len(titles) > 5:
            result_length = 5
        else:
            result_length = len(titles)
        # Build the output tuples
        output = []
        for i in range(result_length):
            output.append(
                {
                    "title": titles[i],
                    "url": SEP_URL + urls[i].lstrip("../")
                }
            )
        self.results = output
        return output
