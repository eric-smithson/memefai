from clarifai_handler import *
from reddit_handler import *

# this is where we do all the main action, we will make call to the other files from this script

# fill out with our message template, will have to be formatted in reddit markup
MESSAGE_TEMPLATE = '''Meme has these tags:
    $__TAGS__$
'''

# get url from reddit
# submission_url = get_submission_url()

# get image url from reddit
# image_url = get_image_post_url()
image_url_list = get_image_post_url()
image_url_list.start()
image_url_list.join()

# send image to clarifai
for image_url in image_url_list:
    image_tags = get_tags(image_url) # this function is defined in clarifai_handler.py

    # format the message template to include the tags
    message = MESSAGE_TEMPLATE.replace(("$__TAGS__$"), (', ').join(image_tags))
    print message

# send comment to reddit to be posted
# make_comment(message)