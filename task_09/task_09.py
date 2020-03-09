from utils import log, random_num, floor
from PIL import Image, ImageFont, ImageDraw, ImageFilter

"""
参考网站：
https://www.kancloud.cn/trent/hotoimagefilter/102786
https://juejin.im/post/5b9e127df265da0a9a395e01
每个点都有对应的颜色，PIL图可以获取和设置每个像素点的颜色。

颜色有两种RGBA和RGB，(r, g, b, a)前者有4个值，后者有3个值，每个都是0到255，RGBA的a就代表透明度。

getpixel((x, y))是获取对应像素点的颜色。
putpixel((x, y), color)是设置对应像素点的颜色。

from PIL import Image

img = Image.open("安娜的橱窗.jpg")
img = img.convert('RGBA') # 修改颜色通道为RGBA
x, y = img.size # 获得长和宽

# 设置每个像素点颜色的透明度
for i in range(x):
    for k in range(y):
        color = img.getpixel((i, k))
        color = color[:-1] + (100, )
        img.putpixel((i, k), color)

img.save("安娜的橱窗_switch.PNG") # 要保存为.PNG格式的图片才可以
 
 注：.PNG格式的图片才支持透明度设置哦！

重点讲一下这段代码：color = color[:-1] + (100, )
因为获取到的color是(r, g, b, 255)这是一个元组，[:-1]是切片，
代表获取前3个元素，就是(r, g, b)，然后再加个(100, )
这是包含一个数元组的写法。加起来就是(r, g, b, 100)达到修改透明度的效果
 
"""


def colors_of_gray(gray):
    g = int(gray)
    t = (g, g, g)
    return t


def grayscale(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            # log("position", position)
            colors = img.getpixel(position)
            # log('colors', colors)
            gray = (colors[0] + colors[1] + colors[2]) / 3
            gray_colors = colors_of_gray(gray)
            img.putpixel(position, gray_colors)
    img.save('grayscale.jpg')
    img.show()
    pass

 
def black_white(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            # log("position", position)
            colors = img.getpixel(position)
            # log('colors', colors)
            gray = (colors[0] + colors[1] + colors[2]) / 3
            if gray >= 100:
                gray = 255
            else:
                gray = 0
            gray_colors = colors_of_gray(gray)
            img.putpixel(position, gray_colors)
    img.save('black_white.jpg')
    img.show()


def negative(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            # log("position", position)
            colors = img.getpixel(position)
            # log('colors', colors)
            r = 255 - colors[0]
            b = 255 - colors[1]
            g = 255 - colors[2]
            rbg = (r, b, g)
            img.putpixel(position, rbg)
    img.save('negative.jpg')
    img.show()


"""
    毛玻璃效果

    在把图片转为黑白图的基础上，获取位置 position 之后，
    使用 random.random() 函数和 int 函数生成一个随机整数 index
    声明一个像素点变量 temp,
    temp 坐标为（i - index, j - index)（坐标不能为负数）
    获取 temp 的 rgba 并赋值给 position 的 rgba
"""


def frosted_glass(img):
    img = img.convert('RGBA')  # 修改颜色通道为RGBA
    w, h = img.size
    for i in range(w - 8):
        for j in range(h - 8):
            position = (i, j)
            index = random_num(0, 8)
            temp = (i + index, j + index)
            colors = img.getpixel(temp)
            # log('colors', colors)
            img.putpixel(position, colors)
    img.save('frosted_glass.png')
    img.show()


def mosaic(img):
    w, h = img.size
    n = 10  # 每块 10 px
    for i in range(w):
        for j in range(h):
            position = (i, j)
            x = floor(i / n) * n
            y = floor(j / n) * n
            temp = (x, y)
            colors = img.getpixel(temp)
            # log('colors', colors)
            img.putpixel(position, colors)
    img.save('mosaic.jpg')
    img.show()
    pass


def colors_of_nostalgia(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = 0.393 * r + 0.769 * g + 0.189 * b
    G = 0.349 * r + 0.686 * g + 0.168 * b
    B = 0.272 * r + 0.534 * g + 0.131 * b
    return (int(R), int(G), int(B))
    pass


def nostalgia(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            # log("position", position)
            colors = img.getpixel(position)
            # log('colors', colors)
            gray_colors = colors_of_nostalgia(colors)
            img.putpixel(position, gray_colors)
    img.save('nostalgia.jpg')
    img.show()


def abs(num):
    if num < 0:
        return -num
    return num


def colors_of_comic_books(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = abs(g - b + g + r) * r / 256
    G = abs(b - g + b + r) * r / 256
    B = abs(b - g + b + r) * g / 256
    return (int(R), int(G), int(B))
    pass


def comic_books(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            gray_colors = colors_of_comic_books(colors)
            img.putpixel(position, gray_colors)
    img.save('comic_books.jpg')
    img.show()


def colors_of_brown(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = r * 0.393 + g * 0.769 + b * 0.189
    G = r * 0.349 + g * 0.686 + b * 0.168
    B = r * 0.272 + g * 0.534 + b * 0.131
    return (int(R), int(G), int(B))
    pass


def brown(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            gray_colors = colors_of_brown(colors)
            img.putpixel(position, gray_colors)
    img.save('brown.jpg')
    img.show()


def colors_of_frozen(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = (r - g - b) * 3 / 2
    G = (g - r - b) * 3 / 2
    B = (b - g - r) * 3 / 2
    return (int(R), int(G), int(B))
    pass


def frozen(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            gray_colors = colors_of_frozen(colors)
            img.putpixel(position, gray_colors)
    img.save('frozen.jpg')
    img.show()


def colors_of_fused_cast(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = r * 128 / (g + b + 1)
    G = g * 128 / (r + b + 1)
    B = b * 128 / (g + r + 1)
    return (int(R), int(G), int(B))
    pass


def fused_cast(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            gray_colors = colors_of_fused_cast(colors)
            img.putpixel(position, gray_colors)
    img.save('fused_cast.jpg')
    img.show()


def colors_of_dark(colors):
    r = colors[0]
    g = colors[1]
    b = colors[2]
    R = r * 128 / (g + b + 1)
    G = g * 128 / (r + b + 1)
    B = b * 128 / (g + r + 1)
    return (int(R), int(G), int(B))
    pass


def dark(img):
    w, h = img.size
    for i in range(w):
        for j in range(h):
            position = (i, j)
            colors = img.getpixel(position)
            gray_colors = colors_of_dark(colors)
            img.putpixel(position, gray_colors)
    img.save('dark.jpg')
    img.show()

def colors_of_mboss(colors1, colors2):
    r = abs(colors1[0] - colors2[0] + 128)
    b = abs(colors1[1] - colors2[1] + 128)
    g = abs(colors1[2] - colors2[2] + 128)
    if r > 255:
        r = 255
    if b > 255:
        b = 255
    if g > 255:
        g = 255
    c = int((r + b + g) / 3)
    return (c, c, c)
    pass


def mboss(img):
    w, h = img.size
    for i in range(w-5):
        for j in range(h-5):
            position = (i, j)
            x = i + 5
            if x > w:
                x = w
            y = j + 5
            if y > h:
                y = h
            position2 = (x, y)
            colors1 = img.getpixel(position)
            # log('colors1', colors1)
            colors2 = img.getpixel(position2)
            # log('colors2', colors2)
            gray_colors = colors_of_mboss(colors1, colors2)
            # log('colors', gray_colors)
            img.putpixel(position, gray_colors)
    img.save('mboss.jpg')
    img.show()

def main():
    img = Image.open("add_number.jpg")
    # grayscale(img)
    # black_white(img)
    # negative(img)
    # frosted_glass(img)
    # mosaic(img)
    # nostalgia(img)
    # comic_books(img)
    # brown(img)
    # frozen(img)
    # fused_cast(img)
    # dark(img)
    # mboss(img)


if __name__ == '__main__':
    main()
