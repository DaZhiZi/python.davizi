from utils import log
"""
第 0022 题：
 iPhone 6、iPhone 6 Plus 早已上市开卖。
请查看你写得 第 0005 题的代码是否可以复用。


跟第五题一样，遍历给出目录下的图片，把大于iPhone5分辨率的图片都进行缩放。
使用Python的PIL库对图片进行处理，IPhone5屏幕分辨率为640 × 1136
，将大于该分辨率的图片按照一定比例缩放至适合大小并保存。
由于第五题已经写过相关函数，就改动一下变成可以根据给出的型号来转换的就行。

https://blog.csdn.net/huangxiongbiao/article/details/46540861
"""
import os
from PIL import Image
size_config = {
    'iPhone5': {
        'h': 1136,
        'w': 640
        },
    'iPhone6': {
        'h': 1334,
        'w': 750
        },
    'iPhone6Plus': {
        'h': 2208,
        'w': 1242
        }
}

def small_image(start_dir, end_dir, filename, phone):
    path = os.path.join(start_dir, filename)
    log('path', path)
    img = Image.open(path)
    p = size_config[phone]
    phone_h = p['h']
    # log('phone_h', phone_h)
    phone_w = p['w']
    while True:
        h, w = img.size
        log('h', h)
        log('w', w)
        if h < phone_h:
            # iphone5分辨率为1136x640
            if w < phone_w:
                break
        img = img.resize((int(h * 0.9), int(w * 0.9)))
        end_path = os.path.join(end_dir, filename)
        log('end_path', end_path)
        img.save(end_path)
        log('保存成功')


def small_images(start_dir, end_dir, phone):
    images = os.listdir(start_dir)
    for image in images:
        filename = image
        log('filename', filename)
        small_image(start_dir, end_dir, filename, phone)


def main():
    start = 'start_image'
    end = 'end_image'
    phone = 'iPhone6Plus'
    small_images(start, end, phone)
    pass


if __name__ == "__main__":
   main()