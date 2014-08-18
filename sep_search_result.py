from constants import SEP_URL

class SEPSearchResult():

    query = None

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