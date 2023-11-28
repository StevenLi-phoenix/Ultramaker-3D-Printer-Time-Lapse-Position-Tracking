import json
import os
import time

import requests
import atexit

os.makedirs("layers", exist_ok=True)

printer_ip = "192.168.236.130"  # change to your printer ip
url = "http://{}/api/v1/printer/heads/0/position".format(printer_ip)

track_x = []
track_y = []
track_z = []

@atexit.register
def save_last():
    global track_x, track_y, track_z
    print("save last")
    print("\nZ = {}".format(last_point[2]), end=": ")
    if os.path.exists("layers/{}.json".format(last_point[2])):
        print("File exists, load and extend")
        data = json.load(open("layers/{}.json".format(last_point[2]), "r"))
        track_x.extend(data["x"])
        track_y.extend(data["y"])
        track_z.extend(data["z"])
    else:
        print("File not exists, create new")
    json.dump({"x": track_x, "y": track_y, "z": track_z}, open("layers/{}.json".format(last_point[2]), "w"))

count = 0

last_point = [0, 0, 0]
while True:
    content = requests.get(url)
    count = (count + 1) % 4
    print("\r{}".format("." * count), end="")
    content_json = content.json()
    if abs(last_point[2] - content_json["z"]) > 0.1:  # toreance 0.1
        # save and clear
        print("\nZ = {} changed".format(last_point[2]), end=": ")
        if os.path.exists("layers/{}.json".format(last_point[2])):
            print("File exists, load and extend")
            data = json.load(open("layers/{}.json".format(last_point[2]), "r"))
            track_x.extend(data["x"])
            track_y.extend(data["y"])
            track_z.extend(data["z"])
        else:
            print("File not exists, create new")
        json.dump({"x": track_x, "y": track_y, "z": track_z}, open("layers/{}.json".format(last_point[2]), "w"))
        track_x.clear()
        track_y.clear()
        track_z.clear()
    if last_point[0] != content_json["x"] or last_point != content_json["y"] or last_point != content_json["z"]:
        print("\r                                     ", end="")
        print("\r     {} {} {}".format(content_json["x"], content_json["y"], content_json["z"]), end="")
        track_x.append(content_json["x"])
        track_y.append(content_json["y"])
        track_z.append(content_json["z"])
    last_point = [content_json["x"], content_json["y"], content_json["z"]]
    time.sleep(0.2)  # 5hz

