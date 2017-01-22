import json
import os
# handles all json interactions

#todo: make sure when this script is run that it creates the neccesary filepaths so it doesn't crash looking for files that aren't there when it runs the first time

def check_if_url_in_db(url):
    with open(log_dir + "/database.json", "r") as log_fp:
        url_dict = json.load(log_fp)
        return url in url_dict


log_dir = os.getcwd() + '/data/logs'

def put_in_db(url, tags, text, title):
    url_dict = {}
    with open(log_dir + "/database.json", "r") as log_fp:
        url_dict = json.load(log_fp)
    log_fp.close()

    temp_dict = {}
    temp_dict["title"] = title
    temp_dict["tags"] = tags
    temp_dict["text"] = text
    url_dict[url] = temp_dict
    with open(log_dir + "/database.json", "w") as log_fp:
        json.dump(url_dict, log_fp, indent=1)
    return

dict = {}

dict["hello"] = "greeting"
dict["swiggity"] = "swoggity"

print dict["hello"]