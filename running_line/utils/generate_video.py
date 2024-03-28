import os
os.environ["IMAGEMAGICK_BINARY"] = f"{os.getcwd()}/running_line/utils/squashfs-root/AppRun"
os.environ["LD_LIBRARY_PATH"] = f"{os.getcwd()}/running_line/utils/squashfs-root/usr/lib"
from moviepy.editor import *

def generate_video(text):
  
        w = 100
        h = w
        moviesize = w,h
        bg_color = (64, 224, 208)
        background = ColorClip(moviesize, bg_color)
        txt = text

        clip_txt = TextClip(txt,color='white', align='West',fontsize=90,
                        font='Ubuntu-Bold', method='label')
        txt_width = clip_txt.size[0]
        txt_speed = (w + txt_width) // 3

        moving_txt = clip_txt.set_position(lambda t: (int(w-t*txt_speed), "center"))

        final = CompositeVideoClip([
                background,
                moving_txt],
                size = moviesize)
        final.set_duration(3).write_videofile("./running_line/video/line.mp4", fps=30, codec="libx264")