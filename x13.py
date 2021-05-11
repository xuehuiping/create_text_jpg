# -*- encoding: utf-8 -*-
"""
@date: 2021/5/11 9:42 上午
@author: xuehuiping
"""
'''生成旋转角度的文字图片'''

import random
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

width = 300
height = 300
font_path = '仿宋_GB2312.ttf'


def draw_text(text, angle):
    '''
    创建图片，中文字体
    :param text: 要绘制的文字
    :param angle: 倾斜角度
    :return:
    '''
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    # 按宽度比例显示文字
    font = ImageFont.truetype(font_path, int(width / len(text)))
    # 白色字体
    draw.text((5, int(height / 3)), text, (0, 0, 255), font=font)

    center = (width / 2, height / 2)  # 中心点
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    img = np.array(img)
    img = cv2.warpAffine(img, M, (width, height), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    cv2.imwrite('imgs/img_{}.jpg'.format(text), img)


def gen_img():
    '''
    按照词表里面的文字，随机生成一些图片
    :return:
    '''
    # 词典
    chars = open('chars.txt').read()
    # 文字的长度
    len = random.randrange(3, 10)
    # 随机选择一些文字
    text = random.choices(chars, k=len)
    text = ''.join(text)
    draw_text(text, random.randrange(-45, 45, 5))


if __name__ == "__main__":

    for i in range(1000):
        gen_img()
