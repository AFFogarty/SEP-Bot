
class SEPSearchResult():

    query = None

    def __init__(self, query):
        self.set_query(query)

    def set_query(self, query):
        self.query = str(query).lower().split()
