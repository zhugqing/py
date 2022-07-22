import cv2
import numpy as np
import json

class CVWorker:

  def cv_img_encoding():
      #图片转cv数据
      img = cv2.imread('img.png')  
      # '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样  
      img_encode = cv2.imencode('.png', img)[1]  
      print(img_encode)
      data_encode = np.array(img_encode)

      # 图片unit8数据转list数据
      data_encode = data_encode.tolist()

      with open('img_encoding.txt', "w") as imgdate:
        json.dump(data_encode, imgdate)

  def cv_img_decoding():
      nums=[]
      with open('img_encoding.txt', "r") as imgdate:
        nums = json.load(imgdate)
      a=np.array(nums, dtype='uint8')
      image=cv2.imdecode(a, cv2.IMREAD_COLOR)
      cv2.imwrite('img_decoding.png', image)

if __name__ == '__main__':
  # 把图片编码成数据
  CVWorker.cv_img_encoding();

  # 把数据解码成图片
  CVWorker.cv_img_decoding();