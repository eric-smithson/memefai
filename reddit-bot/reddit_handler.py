# this where we will build the functions which handle all our reddit interactions
import praw

def get_image_post_url():
    reddit = praw.Reddit(user_agent='MemefaiBot for SwampHacks', client_id='2UscbBFgmqdBMA',
                         client_secret='yY3dSQTQy2tBWTQVi3eW1vuyf-I', username='IAmJimmyNeutron', password='67y890')
    subreddit = reddit.subreddit("me_irl")
    submissions_list = []
    for submission in subreddit.hot(limit=5):
        if submission.score > 500:
            url = submission.url
            if url[7:12] == 'imgur':
                url = 'http://i.' + url[7:] + '.jpg'
            print url
            submissions_list.append(url)
    return submissions_list

def make_comment(body):
    pass
