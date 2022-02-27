import os , glob
from PIL import Image
import cv2
import numpy as np

sizes=[(1428,0,1717,309)]
a=1
for filename in glob.glob('C:/Users/sheis/Desktop/data set cleaning/DataSet/all letter/first cutting/*.*'):
   for i in sizes:
      new = Image.new('RGB',(1100,1100),color='white')
      img=Image.open(filename)
      #img2= img.resize((1275,1754))
      imm=img.crop(box=(i))
      imm1 = imm.resize((400,1000))
      new.paste(imm1,(350,50))
      path="C:/Users/sheis/Desktop/data set cleaning/DataSet/all letter/secound cutting/a2/"+"A_"+str(a)+".png"
      new.save(path)
      
#-------threshold
      src = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
      # Set threshold and maxValue
      thresh = 190
      maxValue = 255
      th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)
      cv2.imwrite(path, dst)



#---crop extra space
      img = cv2.imread(path) # Read in the image and convert to grayscale
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      gray = 255*(gray < 128).astype(np.uint8) # To invert the text to white
      coords = cv2.findNonZero(gray) # Find all non-zero points (text)
      x, y, w, h = cv2.boundingRect(coords) # Find minimum spanning bounding box
      x1 = x-10
      y1 = y-10
      x2 = x+w+10
      y2 = y+h+10
      crop = img[y1:y2, x1:x2]#crop extra space
      resize = cv2.resize(crop, (224, 224))#resise image 
      cv2.imwrite(path, resize) # Save the image
      a+=1