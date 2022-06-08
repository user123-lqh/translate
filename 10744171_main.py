import keyboard             #监听键盘
from PIL import ImageGrab   #图片抓取
from aip import AipOcr      #文字识别
import requests             #发动自动翻译请求
import time

keyboard.wait("Win+Shift+S")  #windows 自帶的截圖工具
print("截屏开始")               #提示用戶開始截圖

keyboard.wait("enter")        #保存圖片結果
print("截屏结束")
time.sleep(0.1)
image = ImageGrab.grabclipboard()  #到系統中找到圖片並存為img.png
image.save('img.png')
APP_ID = '25352377'                     #輸入百度API的賬號密碼
API_KEY = 'Fl34TgEunMQko7kVwCFBBcfb'
SECRET_KEY = 'vqrupEoP7t0qEFlSVRSK8eVCGLyEAK4K'
aipocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)    
with open('img.png', 'rb') as f:
    img = f.read()
    result = aipocr.basicAccurate(img)
    words_result = result['words_result']   #將API文字識別結果存入words_result
    for r in words_result:
        words = r['words']
        print("文字识别结果:" + words)          #print結果
url = "http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i=" + words    #在有道翻譯網站搜索該詞語
resp_json = requests.get(url).json()
translateResult = resp_json['translateResult']              #爬取翻譯結果輸出
for t in translateResult:
    tgt = t[0]['tgt']
    print('自动翻译结果:' + tgt)