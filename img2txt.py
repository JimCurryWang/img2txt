import sys
from PIL import Image as PIL
import pyocr
import pyocr.builders

import sharpened

def main(imgfile,language):
    # pyocr支持两種OCR庫，if 只安装了tesseract，只會獲得tesseract
    tool = pyocr.get_available_tools()[0]

    # 選擇要使用的語言，使用print (tool.get_available_languages() )查看列表
    #https://github.com/tesseract-ocr/tessdata 下載訓練資料 丟進路徑 /usr/local/share
    #print(tool.get_available_languages())
    #['chi_sim'0簡體, 'chi_tra'1繁體, 'eng'2英文, 'osd'3]
    lang = tool.get_available_languages()[0]

    # 對圖像運行OCR，識別圖像中的文本
    txt = tool.image_to_string( PIL.open(imgfile),
                                lang=lang,
                                builder=pyocr.builders.TextBuilder()
                              )
    return(txt)


if __name__ == '__main__':
    #['chi_sim'0簡體, 'chi_tra'1繁體, 'eng'2英文, 'osd'3]
    #EXAMPLE:
    imgfile = sys.argv[1]
    language = sys.argv[2]
    try:
        main(imgfile,language)
        result = main(imgfile,language)
        print(result)
    except Exception as e:
        print('transfer fail',e)