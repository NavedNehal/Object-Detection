import torch 
import cv2
import numpy as np
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
capture = cv2.VideoCapture(0)
while capture.isOpened():
  ret,frame = capture.read()
  results = model(frame)
  cv2.imshow('PERSON', np.squeeze(results.render()))

  if cv2.waitKey(10) & 0xFF == ord('q'):
    break
capture.release()
cv2.destroyAllWindows()
import uuid
import os
import time
IMAGES_PATH = os.path.join('data','images')
labels = ['awake','drowsy']
number_img= 20
cap = cv2.VideoCapture(0)
for label in labels:
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for img_num in range(number_img):
       print('Collecting images for {}, image number {}'.format(label, img_num))
       ret,frame = cap.read()
       
       imgname = os.path.join(IMAGES_PATH,label+'.'+str(uuid.uuid1())+'.jpg')
       cv2.imwrite(imgname, frame)
       cv2.imshow('image Collection', frame)
       time.sleep(2)

    if cv2.waitKey(10) & 0xFF == ord('q'):
       break
capture.release()
cv2.destroyAllWindows()

