import os
import json
import matplotlib.pyplot as plt

layers = [".".join(i.split(".")[:-1]) for i in os.listdir("layers")]
for layer in layers:
    print(layer)
    if not os.path.exists("layers/{}.json".format(layer)):
        raise FileNotFoundError("File not exists")
    data = json.load(open("layers/{}.json".format(layer), "r"))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.plot(data["x"], data["y"], data["z"], c="r", marker='o', alpha=0.25, linewidth=2)
    plt.savefig("plots/{}.jpg".format(layer))
    plt.show()