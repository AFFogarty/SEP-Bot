

class VisitedThreadSet():
    set = None

    def __init__(self):
        self.set = set()

    def load_set(self):
        pass

    def save_set(self):
        pass

    def add(self, value):
        self.set.add(str(value))

    def contains(self, value):
       if str(value) in self.set:
           return True
       else:
           return False
