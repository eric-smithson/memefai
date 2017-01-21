# this where we will build the functions which handle all our reddit interactions

def get_post_url():
    import praw
    reddit = praw.Reddit(user_agent='MemefaiBot for SwampHacks', client_id='2UscbBFgmqdBMA',
                         client_secret='yY3dSQTQy2tBWTQVi3eW1vuyf-I', username='IAmJimmyNeutron', password='67y890')
    subreddit = reddit.subreddit("me_irl")
    for submission in subreddit.hot(limit=5):
        if submission.score > 500:
            print submission.url

def get_post_image_url():
    pass

def make_comment():
    pass
