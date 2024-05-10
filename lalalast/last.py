import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow.keras
import numpy as np
import cv2

f = open("data.txt", 'r')
date = f.readline()
f.close()
date = date[5:]
# 모델 위치
model_filename ='converted_keras\keras_model.h5'
np.set_printoptions(precision=6, suppress=True)

# 케라스 모델 가져오기
model = tensorflow.keras.models.load_model(model_filename,compile=False)

img = cv2.imread("sample.jpg")
size = (224, 224)
img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
img = (img.astype(np.float32) / 127.0) - 1
img = img.reshape((1, 224, 224, 3))

result = model.predict(img)
list = result.tolist()
list2 = []
for i in range(5):
    list2.append(list[0][i]*100)

i = list2.index(max(list2))

if i ==0:
    pr = "감상돔"
    if float(date)>5 and float(date)<6:
        a = "금어기입니다."
    else:
        a = "금어기가 아닙니다."
    r = "포획 가능 길이는 25cm 미만입니다."
elif i ==1:
    pr = "대구"
    if float(date)>1.15 and float(date)<2.16:
        a = "금어기입니다."
    else:
        a = "금어기가 아닙니다."
    r = "포획 가능 길이는 35cm 미만입니다."
elif i ==2:
    pr = "돌돔"
    a = "금어기는 없습니다."
    r = "포획 가능 길이는 24cm 미만입니다."
    
elif i ==3:
    pr = "방어"
    a = "금어기는 없습니다."
    r = "포획 가능 길이는 30cm 미만입니다."
elif i ==4:
    pr = "참가자미"
    a = "금어기는 없습니다."
    r = "포획 가능 길이는 20cm 미만입니다."

f = open("data.txt", 'w')
f.write(pr)
f.write("\n")
f.write(a)
f.write("\n")
f.write(r)
f.close()
