from clarifai_handler import *
from reddit_handler import *
from ocr_handler import *
import json

# this is where we do all the main action, we will make call to the other files from this script

# fill out with our message template, will have to be formatted in reddit markup
MESSAGE_TEMPLATE = '''Memefai_Bot has detected these tags:

    $__TAGS__$$__TEXT_BLURB__$

^(Like this bot? Contribute at github.com/eric-smithson/memefai)
'''
# get url from reddit
# submission_url = get_submission_url()

# get image url from reddit
# image_url = get_image_post_url()
image_url_list = get_image_post_url()

# send image to clarifai
for image_url in image_url_list:
    image_tags = get_tags(image_url) # this function is defined in clarifai_handler.py

    # format the message template to include the tags
    message = MESSAGE_TEMPLATE.replace("$__TAGS__$", (', ').join(image_tags))
    # TODO: the code below is placeholder, needs to be updated with actual OCR calls
    has_text = False
    if(does_image_have_text(image_url)):
        message = message.replace("$__TEXT_BLURB__$", "\n\nDetected text in meme: \n\n    $__TEXT__$.")
        message = message.replace("$__TEXT__$", get_text_in_image(image_url))
    else:
        message = message.replace("$__TEXT_BLURB__$", "")
    print message
    make_comment(message)

# send comment to reddit to be posted
# make_comment(message)