# this where we will build the functions which handle all our reddit interactions
import praw

def get_image_post_url():
    reddit = praw.Reddit(user_agent='MemefaiBot for SwampHacks', client_id='2UscbBFgmqdBMA',
                         client_secret='yY3dSQTQy2tBWTQVi3eW1vuyf-I', username='IAmJimmyNeutron', password='67y890')
    subreddit = reddit.subreddit("me_irl")
    submissions_dict = {}
    for submission in subreddit.hot(limit=5):
        if submission.score > 500:
            url = submission.url
            if url[7:12] == 'imgur':
                url = 'http://i.' + url[7:] + '.jpg'
            print submission.title
            print url
            submissions_dict[url] = submission
    return submissions_dict

def make_comment(message, url):
    from urllib import quote_plus
    reddit = praw.Reddit(user_agent='MemefaiBot for SwampHacks', client_id='2UscbBFgmqdBMA',
                         client_secret='yY3dSQTQy2tBWTQVi3eW1vuyf-I', username='IAmJimmyNeutron', password='67y890')
    reply_template = ''
    url_title = quote_plus(submission.title)
    reply_text = reply_template.format(url_title)
    submission.reply(reply_text)
