from utils import log
"""
 **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
 思路：

1. 通过OS库的listdir列出所有图片；
2. 然后通过PIL库的Image.open打开图片并获取图片大小；
3. 最后进入一个死循环：通过PIL库的Image.resize来缩小图片为原图片的90%，
直到图片大小小于iphone5的分辨率大小，退出循环。

os 系统
属性                说明
system( string )   执行系统命令 cmd
getcwd( )           返回当前工作目录
chdir( path )       改变工作目录
listdir( path='.' )  目录中的文件名生成列表
rename( old, new )   将文件 old 重命名 new
"""
import os
from PIL import Image

def small_image(start_dir, end_dir, filename):
    path = os.path.join(start_dir, filename)
    log('path', path)
    img = Image.open(path)
    while True:
        h, w = img.size
        log('h', h)
        log('w', w)
        if h < 1136:
            # iphone5分辨率为1136x640
            if w < 640:
                break
        img = img.resize((int(h * 0.9), int(w * 0.9)))
        end_path = os.path.join(end_dir, filename)
        log('end_path', end_path)
        img.save(end_path)
        log('保存成功')


def small_images(start_dir, end_dir):
    images = os.listdir(start_dir)
    for image in images:
        filename = image
        log('filename', filename)
        small_image(start_dir, end_dir, filename)


def main():
    start = 'start_image'
    end = 'end_image'
    small_images(start, end)
    pass


if __name__ == "__main__":
   main()

