from PIL import Image, ImageDraw, ImageFont
"""
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。
类似于图中效果
分析问题：

通过分析题目可以得知，本题是在图片上面进行的操作，应该是两个图层，一个是ＱＱ头像（固定的），
另外一个是红色数字（可变的），需要用到python的ＰＩＬ模块来处理图像问题。

"""
def image(file_path):
    return Image.open(file_path) #新建绘图对象

def image_draw(img):
    return ImageDraw.Draw(img)

"""
print(img.getpixel((0,0))) #得到像素：
#img读出来的图片获得某点像素用getpixel((w,h))可以直接返回这个点三个通道的像素值
"""

def add_number(num, file_path):
    img = image(file_path)

    h, w = img.size
    size = int(h / 4)  # 字体大小
    # 确定字体格式和字体大小
    font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMYOU.TTF", size)

    draw = image_draw(img)
    x = w - size
    y = 0
    coordinate = (x, y)  # 坐标
    txt = str(num)
    color = (256, 0, 0) # 颜色
    draw.text(coordinate, txt, color , font) # 确定显示的 位置，数字，颜色，字体
    del draw       # 结束画图

    img.save('add_number.jpg')
    img.show()

def main():
    num = 24
    add_number(num, 'img/kobe.jpg')


if __name__ == '__main__':
    main()
