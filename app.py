#!/usr/bin/env python3

# from flask import Flask
from PIL import Image
from PIL import ImageShow

# app = Flask(__name__)


# @app.route('/')
# def hello_world():
    # return 'Hello World!'

image_path = "/usr/share/load-image/barto-image.gif"

image = Image.open(image_path)

# Display the PNG image
ImageShow.show(image)

# Keep the script running until the user closes the image
try:
    while True:
        pass
except KeyboardInterrupt:
    pass