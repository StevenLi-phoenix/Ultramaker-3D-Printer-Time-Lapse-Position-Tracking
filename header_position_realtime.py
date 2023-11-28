import os
import time

import requests
import matplotlib.pyplot as plt

os.makedirs("plots", exist_ok=True)

printer_ip = "192.168.236.130"  # change to your printer ip
url = "http://{}/api/v1/printer/heads/0/position".format(printer_ip)

content = requests.get(url)
content_json = content.json()

# track_x = [content_json["x"]] * 64  # last 64 positions
# track_y = [content_json["y"]] * 64  # last 64 positions
# track_z = [content_json["z"]] * 64  # last 64 positions
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# print(track_x, track_y, track_z)
last_point = [content_json["x"], content_json["y"], content_json["z"]]
while True:
    content = requests.get(url)
    print(content.json())
    # put one in the front, remove one from the end
    content_json = content.json()
    # track_x = track_x[1:] + [content_json["x"]]
    # track_y = track_y[1:] + [content_json["y"]]
    # track_z = track_z[1:] + [content_json["z"]]
    # plot the track in animation in a 3D plot
    # if last != current: plot
    if last_point[0] != content_json["x"] or last_point != content_json["y"] or last_point != content_json["z"]:
        ax.plot([last_point[0],content_json["x"]], [last_point[1],content_json["y"]],
                [last_point[2],content_json["z"]], c="r", marker='o', alpha=0.25, linewidth=2)
        plt.pause(0.01)
    if abs(last_point[2] - content_json["z"]) > 0.1: # toreance 0.1
        print("Z changed")
        # plot save
        plt.savefig("plots/{}.jpg".format(last_point[2]))
        # clear
        ax.clear()

    last_point = [content_json["x"], content_json["y"], content_json["z"]]

    time.sleep(0.1)  # avoid too many requests in a short time overloading the server
