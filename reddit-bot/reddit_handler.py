# this where we will build the functions which handle all our reddit interactions
import praw
import os

def get_image_post_url():
    reddit = praw.Reddit(user_agent='MemefaiBot for SwampHacks', client_id='2UscbBFgmqdBMA',
                         client_secret='yY3dSQTQy2tBWTQVi3eW1vuyf-I', username='MemefaiBot', password=get_password())
    subreddit = reddit.subreddit("me_irl")
    submissions_dict = {}
    for submission in subreddit.hot(limit=150):
        if submission.score > 500:
            url = submission.url
            if url[7:12] == 'imgur':
                url = 'http://i.' + url[7:] + '.jpg'
            if url.__contains__("gallery"):
                continue
            print submission.title
            print url
            submissions_dict[url] = submission
    return submissions_dict

def make_comment(message, submission):
    from urllib import quote_plus
    reddit = praw.Reddit(user_agent='MemefaiBot for SwampHacks', client_id='2UscbBFgmqdBMA',
                         client_secret='yY3dSQTQy2tBWTQVi3eW1vuyf-I', username='MemefaiBot', password=get_password())
    reply_template = message
    # url_title = quote_plus(submission.title)
    # reply_text = reply_template.format(url_title)
    return submission.reply(message)

def get_password():
    with open(os.getcwd() + "/data/password.txt", "r") as pass_fp:
        return pass_fp.read()
