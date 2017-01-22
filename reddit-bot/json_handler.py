import json
import os
# handles all json interactions

#todo: make sure when this script is run that it creates the neccesary filepaths so it doesn't crash looking for files that aren't there when it runs the first time

def check_if_url_in_db(url):
    with open(log_dir + "/database.json", "r") as log_fp:
        url_dict = json.load(log_fp)
        return url in url_dict

def put_in_db(url, tags, text, title, id):
    url_dict = {}
    with open(log_dir + "/database.json", "r") as log_fp:
        url_dict = json.load(log_fp)
    log_fp.close()

    temp_dict = {}
    temp_dict["title"] = title
    temp_dict["tags"] = tags
    temp_dict["text"] = text
    temp_dict["id"] = id
    url_dict[url] = temp_dict
    with open(log_dir + "/database.json", "w") as log_fp:
        json.dump(url_dict, log_fp, indent=1)
    return

# creates database & directories if they don't exist

dir = os.getcwd()
log_dir = dir + '/data/logs'
if not os.path.exists(dir + '/data'):
    os.makedirs(dir + '/data')
if not os.path.exists(dir + '/data/logs'):
    os.makedirs(dir + '/data/logs')
if not os.path.exists(dir + '/data/logs/database.json'):
    with open(dir + '/data/logs/database.json', "w") as log_fp:
        json.dump({}, log_fp)
