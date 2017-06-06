dist 資料夾下 pyimg2txt

一.
[Python3.5 +  + Keras]測試安裝環境為 Mac/OSX10 /Python3.5

OCR（Optical Character Recognition）文字識別
Target : 將圖片做前處理，作為輸入，從中輸出文本 

二.
安裝套件：
1.
$ pip install pytesseract ? 
ps: 不知道要不要裝？？？ anaconda得很怪 改用brew os專用管理器 若為 windows 要裝別的

2.
$ pip install pyocr

3.
$ pip install pillow (pillow anaconda自帶)

4.
Wand itself can be installed from PyPI using pip:
$ pip install Wand

5.
Wand is a Python binding of ImageMagick, so you have to install it as well:

install Homebrew 管理套件first:

6.
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

need Homebrew to install ImageMagick:

$ brew install imagemagick

If seam carving (Image.liquid_rescale()) is needed you have install liblqr as well:

$ brew install imagemagick —with-liblqr

In the end :
$ brew install tesseract


———————————————————————————————————————
tesseract ( OCR庫 命令在python外執行 )
pyocr     (tesseract  python 庫的接口 ) import pyocr
pillow   （p3從python圖像庫PIL分出來的 )  from PIL import Image as PI
imagemagick
wand      (imagemagick python 庫的接口 ) pdf=>image  from wand.image import image
———————————————————————————————————————


三.
<使用說明>
1.img2txt.py
command line>>python img2txt.py 圖片路徑 分析語言
#將圖片做ocr 文字辨識
＃分析語言可選擇三種:[‘chi_sim'0簡體, 'chi_tra'1繁體, 'eng'2英文, 'osd'3]

2.sharpened.py

command line>>python sharpened.py 圖片路徑
＃將圖片做去干擾線灰階處理 並將其儲存 命名為 ‘sharpened_picname’
