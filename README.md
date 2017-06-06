# img2txt
img2txt is base on pyocr-tesseract,witch can transfer img form file to txt.

img2txt 基於 pyocr 接口 tesseract, 對圖像運行OCR，識別圖像中的文本

1.pyocr支持两種OCR庫，如果只安装了tesseract，只會獲得tesseract
2.選擇要使用的語言，使用print (tool.get_available_languages() )查看列表
    #https://github.com/tesseract-ocr/tessdata 下載訓練資料 丟進路徑 /usr/local/share
    #print(tool.get_available_languages())
    #['chi_sim'0簡體, 'chi_tra'1繁體, 'eng'2英文, 'osd'3]
