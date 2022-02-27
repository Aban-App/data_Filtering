import os , glob
from PIL import Image
import cv2
import numpy as np

path = 'C:/Users/sheis/Desktop/data set cleaning/DataSet/abjd letter/*.*'
img_number = 1
for file in glob.glob(path):
      img = cv2.imread(file)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      gray = 255*(gray < 128).astype(np.uint8) # To invert the text to white
      coords = cv2.findNonZero(gray) # Find all non-zero points (text)
      x, y, w, h = cv2.boundingRect(coords) # Find minimum spanning bounding box
      x1 = x+173
      y1 = y+133
      x2 = x+w-173
      y2 = y+h-133
      crop = img[y1:y2, x1:x2]#crop extra space
      cv2.imwrite("C:/Users/sheis/Desktop/data set cleaning/DataSet/abjd letter/first cutting/"+"ABJD_"+str(img_number)+".png", crop) # Save the image
      img_number += 1