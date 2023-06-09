import cv2
import numpy as np
from PIL import Image
from PIL import ImageFont, ImageDraw
# import matplotlib.pyplot as plt

def text_to_mp4(text: str, vid_name: str, dur: int):
    """
    :param path_img: путь к изображению
    :param vid_name: имя результирующего видео mp4
    :param dur: время длительности клипа в секундах
    """
    f_size = 100
    font = ImageFont.truetype("arial.ttf", f_size)

    f_rate = 30.0
    img = Image.new(mode="RGBA", size=(100, 100))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_scr = cv2.VideoWriter(f"{vid_name}.mp4", fourcc, f_rate, (img.width, img.height))

    h_size = dur * int(f_rate)
    h = font.getlength(text) / h_size
    i = 0
    for im in range(0, h_size):
        img = Image.new(mode="RGBA", size=(100, 100))
        draw = ImageDraw.Draw(img)
        draw.text((i, 0), text, font=font)
        frame = np.array(img)
        frame_buf = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        i -= h
        out_scr.write(frame_buf)


if __name__ == '__main__':
    text_to_mp4(text='0123456789', vid_name='out_put', dur=3)
