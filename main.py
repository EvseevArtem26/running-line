import os
os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/magick"
import numpy as np
from moviepy.editor import *
from moviepy.video.tools.drawing import color_gradient
import moviepy.video.fx.all as vfx
from skimage import transform as tf



# RESOLUTION

w = 100
h = w
moviesize = w,h
bg_color = (64, 224, 208)



# THE RAW TEXT
txt = "Hello world!"

# CREATE THE TEXT IMAGE


clip_txt = TextClip(txt,color='white', align='West',fontsize=90,
                    font='Ubuntu-Bold', method='label')


# SCROLL THE TEXT IMAGE BY CROPPING A MOVING AREA

txt_width = clip_txt.size[0]
txt_speed = (w + txt_width)//3

# print("speed:", txt_speed)

# moving_txt = clip_txt.set_position(w, "center")
moving_txt = clip_txt.set_position(lambda t: (int(w-t*txt_speed), "center"))


background = ColorClip(moviesize, bg_color)

# COMPOSE THE MOVIE

final = CompositeVideoClip([
        background,
        moving_txt],
        size = moviesize)


# WRITE TO A FILE

final.set_duration(3).write_videofile("./video/line.mp4", fps=30, codec="libx264")