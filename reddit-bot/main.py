from clarifai_handler import *
from reddit_handler import *
from ocr_handler import *
from json_handler import *
import json

# this is where we do all the main action, we will make call to the other files from this script

# fill out with our message template, will have to be formatted in reddit markup
MESSAGE_TEMPLATE = '''MemefaiBot has detected these tags:

    $__TAGS__$$__TEXT_BLURB__$

^(Like this bot? Contribute at github.com/eric-smithson/memefai)
'''

# get image url from reddit
image_url_list = get_image_post_url()

# todo: find a way to get the titles, this is actually important because the titles differ with the spacing between "me" and "irl", usually with emoji.

# send image to clarifai
for image_url in image_url_list:

    if check_if_url_in_db(image_url): # returns true if the url is already in our db
        continue

    image_tags = get_tags(image_url) # this function is defined in clarifai_handler.py

    # format the message template to include the tags
    message = MESSAGE_TEMPLATE.replace("$__TAGS__$", (', ').join(image_tags))

    # TODO: build out OCR calls
    text_in_image = ""
    if(does_image_have_text(image_url)):
        message = message.replace("$__TEXT_BLURB__$", "\n\nDetected text in meme: \n\n    $__TEXT__$.")
        text_in_image = get_text_in_image(image_url)
        message = message.replace("$__TEXT__$", text_in_image)
    else:
        message = message.replace("$__TEXT_BLURB__$", "")

    print message

    # sends info to be stored in the database
    put_in_db(image_url, image_tags, text_in_image)

    # sends comment to reddit to be posted
    make_comment(message)