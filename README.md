# img2txt
img2txt is base on pyocr-tesseract,witch can transfer img form file to txt.

img2txt.py 基於 pyocr 接口 tesseract, 對圖像運行OCR，識別圖像中的文本

**img2txt.py**

    ```
    command line>>python img2txt.py 圖片路徑 分析語言
    ```

   將圖片做ocr 文字辨識

   分析語言可選擇三種:[‘chi_sim'0簡體, 'chi_tra'1繁體, 'eng'2英文, 'osd'3]

- 1-1.pyocr支持两種OCR庫，如果只安装了tesseract，只會獲得tesseract

- 1-2.選擇要使用的語言，使用print (tool.get_available_languages() )查看列表

    (https://github.com/tesseract-ocr/tessdata )下載訓練資料 丟進路徑 /usr/local/share

    ```
    print(tool.get_available_languages())
    ```

    ['chi_sim'0簡體, 'chi_tra'1繁體, 'eng'2英文, 'osd'3 ]
    
    
 **sharpened.py**

    ```
    command line>>python sharpened.py 圖片路徑
    ```

將圖片做去干擾線灰階處理 並將其儲存 命名為 ‘sharpened_picname’

