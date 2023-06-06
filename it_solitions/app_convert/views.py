from django.shortcuts import render
from django.http import FileResponse
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFont, ImageDraw
from django.http import HttpResponse, Http404


def download_file():
    print("DOWN")
    fl_path = './app_convert/'
    filename = 'out_put.mp4'
    fl = open(fl_path+filename, 'r')
    some_file_path = './app_convert/out_put.mp4'
    with open(some_file_path, mode="rb") as file_like:
        print("File = {}".format(file_like))
        # mime_type, _ = mimetypes.guess_type(fl_path)
        response = HttpResponse(file_like, content_type="video/mp4")
        response['Content-Disposition'] = "attachment; filename=" + str(filename)
        # print(response)
        return response


def text_to_mp4(text: str, vid_name: str = 'out_put', dur: int = 3):
    """
    :param text: строка
    :param vid_name: имя результирующего видео mp4
    :param dur: время длительности клипа в секундах
    """
    f_size = 100
    font = ImageFont.truetype("arial.ttf", f_size)

    f_rate = 30.0
    img = Image.new(mode="RGBA", size=(100, 100))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_scr = cv2.VideoWriter(f"./app_convert/{vid_name}.mp4", fourcc, f_rate, (img.width, img.height))

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


def index(request):
    text = request.GET.get("text")
    print(text)
    out_put = 'out_put'
    text_to_mp4(text=text, vid_name=out_put)
    return download_file()
