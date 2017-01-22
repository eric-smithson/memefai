from clarifai_handler import *
from reddit_handler import *
from ocr_handler import *
from json_handler import *
import time

MESSAGE_TEMPLATE = '''MemefaiBot has detected these tags:

    $__TAGS__$$__TEXT_BLURB__$$__EMOJI__$

^(This bot uses) ^[Clarifai](https://www.clarifai.com/), ^(a convolutional neural net API, to automatically find and recognize elements present in even the spiciest memes. Like this bot? Contribute ) ^[here](https://github.com/eric-smithson/memefai)!
'''


def title_stripper(title):
    if(title[0:2].lower() == "me" and title[-3:].lower() == "irl"):
        return title[2]
    else:
        return ""

while(True):
    # get image url from reddit
    image_url_dict = get_image_post_url()

    # send image to clarifai
    # todo: have it pick out the top rated comment instead of picking one at random
    for image_url, submission in image_url_dict.items():
        if check_if_url_in_db(image_url): # returns true if the url is already in our db
            print "already in database: " + image_url
            continue

        image_tags = get_tags(image_url) # this function is defined in clarifai_handler.py
        print image_tags.__sizeof__()
        for i in range(5, image_tags.__len__(), 5):
            image_tags[i] = "\n    " + image_tags[i]

        # format the message template to include the tags
        message = MESSAGE_TEMPLATE.replace("$__TAGS__$", (', ').join(image_tags))

        # TODO: build out OCR handler
        text_in_image = ""
        if(does_image_have_text(image_url)):
            message = message.replace("$__TEXT_BLURB__$", "\n\nDetected text in meme: \n\n    $__TEXT__$.")
            text_in_image = get_text_in_image(image_url)
            message = message.replace("$__TEXT__$", text_in_image)
        else:
            message = message.replace("$__TEXT_BLURB__$", "")

        # build emoji message
        emoji_char = "" #title_stripper(submission.title)

        if emoji_char == "" or emoji_char == "_" or emoji_char == " ":
            message = message.replace("$__EMOJI__$", "")
        else:
            message = message.replace("$__EMOJI__$", "\n\nTitle Emoji: " + emoji_char)

        print message

        print "URL: " + image_url + "\nsubmission.id: " + submission.id

        # try:
        # sends comment to reddit to be posted
        reply_id = make_comment(message, submission)

        # sends info to be stored in the database
        put_in_db(image_url, image_tags, text_in_image, submission.title, submission.id)
        # except:
        #     pass
        break

    time.sleep(120)

