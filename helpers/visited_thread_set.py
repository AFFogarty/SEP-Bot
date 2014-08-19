import json


class VisitedThreadSet():
    file_name = "visited_threads.txt"
    set = None

    def __init__(self):
        self.set = set()
        self.load_set()

    def load_set(self):
        file = open(self.file_name, 'r')
        name_array = json.load(file)
        self.set = set(name_array)
        print self.set

    def save_set(self):
        file = open(self.file_name, 'w')
        json.dump(list(self.set), file)
        file.close()

    def add(self, value):
        self.set.add(str(value))

    def contains(self, value):
       if str(value) in self.set:
           return True
       else:
           return False
