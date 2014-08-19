

class PostFormatter():
    introduction_string = "For more information, consider the following articles:"
    warning_string = "*SEP-Bot is experimental and might return strange results.  Please report bugs at /r/SEPBot.*"
    sep_description = "The Stanford Encyclopedia of Philosophy is a collection of articles written by professional Philosophers."

    def relevant_articles_post(self, results):
        return "{0}\n\n{1}\n\n{2}".format(
            self.introduction_string,
            self.results_list(results),
            self.warning_string
        )

    def results_list(self, results):
        list = ""
        for result in results:
            list += "* [{0}]({1})\n\n".format(
                result["title"].encode('utf-8'),
                result["url"].encode('utf-8')
            )
        return list
