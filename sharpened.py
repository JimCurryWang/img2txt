import sys
import os 
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image,ImageEnhance,ImageFilter

#example
#img_name = "/Users/wangchenyu/Desktop/百寶箱/workfile/OCR/img2txt/picfortest.jpg"

def get_filename(img_name):
    name = os.path.basename(img_name) 
    return name

def image_sharpened(img_name):
    #去除干擾線
    im = Image.open(img_name)
    #圖像二值化
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    data = im.getdata()
    w,h = im.size
    #im.show()
    black_point = 0
    for x in range(1,w-1):
        for y in range(1,h-1):
            #中央像素點的像素值
            mid_pixel = data[w*y+x] 
            #找出上下左右四個方向像素點的像素值
            if mid_pixel == 0: 
                top_pixel = data[w*(y-1)+x]
                left_pixel = data[w*y+(x-1)]
                down_pixel = data[w*(y+1)+x]
                right_pixel = data[w*y+(x+1)]

                #判斷上下左右的黑色像素點總個數
                if top_pixel == 0:
                    black_point += 1
                if left_pixel == 0:
                    black_point += 1
                if down_pixel == 0:
                    black_point += 1
                if right_pixel == 0:
                    black_point += 1
                if black_point >= 3:
                    im.putpixel((x,y),0)
                #print(black_point)
                black_point = 0
    return im

if __name__=='__main__':    
    img_name = sys.argv[1]
    try:
        name = get_filename(img_name)
        im = image_sharpened(img_name)
        #im.show()
        #保存過濾的圖像 
        #命名格式：image_sharpened: s+origin name
        savename = 'sharpened_'+ name
        im.save( savename, 'JPEG' )
        print('Save the file as '+ savename)
    except Exception as e:
        print('Transfer Fail',e)
    