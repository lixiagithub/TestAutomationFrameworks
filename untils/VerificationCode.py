# coding = utf-8
# Author:李昰 
# Date：2021/1/8 14:29

import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
import time  # 代码运行停顿
import requests
import base64
from untils.readYaml import baseConfig

class VerificationCode():

    def __init__(self):
        pass

    def get_pictures(self, img):
        # self.driver.get('http://123.255.123.3')  # 打开登陆页面
        # self.driver.save_screenshot('./login.png')  # 全屏截图
        # page_snap_obj = Image.open('./login.png')
        #img = self.find_element('#pic')  # 定位验证码图片元素
        page_snap_obj = Image.open(baseConfig.picturePath+r'\login.png')
        time.sleep(1)
        location = img.location
        size = img.size  # 获取验证码的大小参数
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']
        image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        #image_obj.show()  # 打开切割后的完整验证码
        #self.driver.close()  # 处理完验证码后关闭浏览器
        return image_obj

    def processing_image(self,img):
        image_obj = self.get_pictures(img)  # 获取验证码
        img = image_obj.convert("L")  # 转灰度
        pixdata = img.load()
        w, h = img.size
        threshold = 160
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        return img

    def delete_spot(self,img):
        images = self.processing_image(img)
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        # images.show()
        return images

    def image_str(self, img):
        image = self.delete_spot(img)
        #image.show()
        image.save(baseConfig.picturePath+r'\verification.png')
        '''
           通用文字识别（高精度含位置版）
           '''
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
        # 二进制方式打开图片文件
        f = open(baseConfig.picturePath+r'\verification.png', 'rb')
        my_img = base64.b64encode(f.read())
        params = {"image": my_img}
        access_token = '24.657e639953d9de82334251bb5167f00f.2592000.1613020536.282335-23524868'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        res=response.json()
        my_code=res['words_result'][0]['words']#获取的是加法例如1+1
        # pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
        # result = pytesseract.image_to_string(image)  # 图片转文字
        # resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
        # result_four = resultj[0:4]  # 只获取前4个字符
        # print(resultj)  # 打印识别的验证码
        print(my_code,res,eval(my_code[0:3]))
        return eval(my_code[0:3])#返回运算结果

    # from aip import AipOcr
    # from os import path
    # def baiduOCR(self,img):  # picfile:图片文件名 outfile:输出文件
    #     filename = image = self.delete_spot(img)  # 图片名称
    #     # 百度提供
    #     """ 你的 APPID AK SK """
    #     APP_ID = ''  # 这是你产品服务的appid
    #     API_KEY = ''  # 这是你产品服务的appkey
    #     SECRET_KEY = ''  # 这是你产品服务的secretkey
    #     client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #     i = open(picfile, 'rb')
    #     img = i.read()
    #
    #     print("正在识别图片：\t" + filename)
    #     """ 调用通用文字识别（高精度版） """
    #     message = client.basicAccurate(img)
    #     print("识别成功！")
    #     i.close()
    #     with open(outfile, 'a+') as fo:  # 这边是写进.txt文件
    #         fo.writelines("*" * 60 + '\n')  # 搞点花里胡哨的做区分
    #         fo.writelines("识别图片：\t" + filename + "\n" * 2)
    #         fo.writelines("文本内容：\n")
    #         # 输出文本内容
    #         for text in message.get('words_result'):  # 识别的内容
    #             fo.writelines(text.get('words') + '\n')
    #         fo.writelines('\n' * 2)
    #     print("文本导出成功！")
    #     print()

if __name__ == '__main__':
    a = VerificationCode()
    img=''#验证码元素的位置
    a.image_str(img)
    print(a.image_str(img))