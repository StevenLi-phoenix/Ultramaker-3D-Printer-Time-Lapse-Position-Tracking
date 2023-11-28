# Ultramaker 3D Printer Time-Lapse & Position Tracking

This project is a Python-based application that tracks the position of a 3D printer head in real-time and generates plots and videos based on the collected data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher
- Libraries: `requests`, `matplotlib`, `numpy`, `cv2`, `pytz`

You can install the necessary libraries using pip:

```bash
pip install requests matplotlib numpy opencv-python pytz
```

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/StevenLi-phoenix/Ultramaker-3D-Printer-Time-Lapse-Position-Tracking.git
```

Navigate to the project directory:

```bash
cd Ultramaker-3D-Printer-Time-Lapse-Position-Tracking
```

## Usage

The project consists of several Python scripts that perform different tasks:

- `main.py`: This script captures images from a 3D printer and saves them to the `images` directory.
- `video_generator.py`: This script reads the images saved by `main.py` and generates a video.
- `header_position_realtime.py`: This script tracks the position of the 3D printer head in real-time and generates a 3D plot.
- `header_position.py`: This script tracks the position of the 3D printer head and saves the data to the `layers` directory.
- `plot_layer.py`: This script reads the data saved by `header_position.py` and generates 3D plots.

### Start capturing images

To start capturing images, modify the `main.py` script to include the IP address of your 3D printer:

```python
...
# IP address of the 3D printer
ip = "xxx.xxx.xxx.xxx"
...
```

Then, run the script:

```bash
python main.py
```

### Generate a video

To generate a video, run the `video_generator.py` script:

```bash
python video_generator.py
```

### Track the position of the 3D printer head in real-time

To track the position of the 3D printer head in real-time, run the `header_position_realtime.py` script:

```bash
python header_position_realtime.py
```

### Track the position of the 3D printer head

To track the position of the 3D printer head, run the `header_position.py` script:

```bash
python header_position.py
```

### Generate 3D plots

To generate 3D plots, run the `plot_layer.py` script:

```bash
python plot_layer.py
```

## Contributing

The project is archived and no longer accepting contributions.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- Thanks to the open-source community for the libraries used in this project.
