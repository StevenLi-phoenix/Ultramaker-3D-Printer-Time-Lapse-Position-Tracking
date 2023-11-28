import os
import time

import requests
import datetime
import pytz  # EST timezone
import json
import atexit
from typing import Any

printer_ip = "192.168.236.130"  # change to your printer ip
url = "http://{}:8080/?action=snapshot".format(printer_ip)

os.makedirs("images", exist_ok=True)


def try_load(filename, fallback: Any = 0):
    if os.path.isfile(filename):
        return json.load(open(filename, "r"))
    else:
        return fallback


content_cache = None
count = try_load("count.json", 0)
info = try_load("info.json", {})


@atexit.register
def exit_handler():
    print('Exit')
    json.dump(info, open("info.json", "w"))
    json.dump(count, open("count.json", "w"))


while True:
    current_time = datetime.datetime.now(pytz.timezone('US/Eastern'))
    content = requests.get(url)
    # print(content.headers)
    # if different then save to images/seq.jpg
    img = content.content
    if content_cache != img:
        content_cache = img
        count += 1
        info[count] = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Save to images/{}.jpg".format(count))
        with open("images/{}.jpg".format(count), "wb") as f:
            f.write(img)
    time.sleep(1)  # avoid too many requests in a short time overloading the server
