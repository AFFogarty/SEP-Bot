import time
from helpers.visited_thread_set import VisitedThreadSet
from helpers.post_formatter import PostFormatter
from praw.errors import APIException
from sep.sep_search_result import SEPSearchResult
import praw
import authentication
import logging

# Logging
logging.basicConfig(filename="sep-bot.log",
                    level=logging.INFO,
                    format='%(asctime)s %(message)s')

r = praw.Reddit('SEP-Bot by /u/StealthSilver')
r.login(authentication.username, authentication.password)

# The subreddit used by the sep bot
sep_bot_subreddit = r.get_subreddit("SEPBot")
test_thread = r.get_submission(submission_id="2dwcwi")
formatter = PostFormatter()
search = None
already_done = VisitedThreadSet()

subreddit = r.get_subreddit('askphilosophy')
for submission in subreddit.get_hot(limit=300):
    op_text = submission.selftext.lower()
    if not already_done.contains(submission.id):
        print "\n\n-----------------------------------\n\n"
        title = u"{0}".format(submission.title)
        print "\n{0}\n".format(title.encode('utf-8'))
        search = SEPSearchResult(title)
        results = search.request_results()
        new_post = formatter.relevant_articles_post(results)
        try:
            submission.add_comment(new_post)
            already_done.add(submission.id)
            already_done.save_set()
        except APIException, e:
            error_message = "Error on submission {0}: {1}".format(submission.id, e)
            print error_message
            logging.info(error_message)
    time.sleep(600)
    # time.sleep(1800)
already_done.save_set()