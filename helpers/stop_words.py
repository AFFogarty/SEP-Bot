import json


class StopWordFilter():
    file_name = "stop_words.json"
    stop_word_set = None

    def __init__(self):
        self.stop_word_set = set()
        self._load_stop_words()

    def _load_stop_words(self):
        try:
            file = open(self.file_name, 'r')
        except IOError:
            return
        word_array = json.load(file)
        self.stop_word_set = set(word_array)

    def filter(self, word_list):
        output = []
        for word in word_list:
            if word not in self.stop_word_set:
                output.append(word)
        return output
