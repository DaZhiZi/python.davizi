from utils import log, random_num
from PIL import Image, ImageFont, ImageDraw, ImageFilter
"""
第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
字母验证码图片:

- 思路：
    - 新建绘图对象：
        - 开始画图
            - 字体格式和字体大小
            - 坐标
            - 背景颜色
            - 文本信息
                - 数字
                    - 颜色
                    - 大小
                - 字母
                    - 颜色
                    - 大小
        - 结束画图
            - 删除 draw
        - 保存图片
            - 保存 photo 
            
    - 生成一个随机 char
    - 生成一个随机 tuple 颜色 rbg
"""
"""
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> import random
>>> random.choice(string.ascii_letters)
'j'
"""
def generate_char():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    r = lower + upper + num
    l = len(r) - 1
    import random
    n = random.randint(0, l)
    char = r[n]
    return char

def generate_color():
    r = random_num(64, 200)
    b = random_num(64, 200)
    g = random_num(64, 200)
    return (r, g, b)


def image(file_path):
    return Image.open(file_path) #新建绘图对象

def image_draw(img):
    return ImageDraw.Draw(img)

def background(num):
    h = 60
    w = h * num
    img = Image.new('RGB', (w, h), (255, 255, 255))
    draw = image_draw(img)

    for x in range(w):
        for y in range(h):
            draw.point((x, y), fill=generate_color())
            # 画布随机加噪点
    img = img.filter(ImageFilter.SMOOTH)
    return img

def draw_char(draw, x, y):
    x = x
    y = 0
    coordinate = (x, y)  # 坐标
    txt = generate_char() # char
    color = generate_color()  # 颜色 color
    # 确定字体格式和字体大小
    font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMYOU.TTF", size=44)
    draw.text(coordinate, txt, color, font)  # 确定显示的 位置，数字，颜色，字体


def passward(num):
    img = background(num) # bg

    draw = image_draw(img)
    for i in range(num):
        x = 60 * i + 10
        y = 0
        draw_char(draw, x, y)

    del draw       # 结束画图
    img.save('passward.png')
    img.show()

def main():
    passward(4)
    pass


if __name__ == '__main__':
    main()
