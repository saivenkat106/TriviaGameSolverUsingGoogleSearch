"""# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm

import pytesseract

# importing OpenCV
import cv2

from PIL import ImageGrab


def imToString():

	# Path of tesseract executable
	pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
	while(True):

		# ImageGrab-To capture the screen image in a loop.
		# Bbox used to capture a specific area.
		cap = ImageGrab.grab(bbox =(700, 300, 1400, 900))

		# Converted the image to monochrome for it to be easily
		# read by the OCR and obtained the output String.
		tesstr = pytesseract.image_to_string(
				cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
				lang ='eng')
		print(tesstr)

# Calling the function
imToString()"""

#a=Image.open('locoimage2.png')
#print(a.show())
#text=tess.image_to_string(a)
#print(text)
#img2=a.crop((40,221,256,65))
#img2.save("img2.jpg")
#40,221,256,65
#this code is used to find coordinates of a particular part of an image
#img=cv2.imread('locoimage1.png',cv2.IMREAD_COLOR)
#roi=cv2.selectROI(img)
#print(roi)
import cv2
import pytesseract
import requests
from bs4 import BeautifulSoup
import webbrowser
pytesseract.pytesseract.tesseract_cmd =r'C:\Users\saive\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

image = cv2.imread('locoimage1.png', 0)
thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

x,y,w,h = 50,213,249,71  
ROI = thresh[y:y+h,x:x+w]
question = pytesseract.image_to_string(ROI, lang='eng',config='--psm 6')
print(question[:-1])
a,b,c,d=48,297,256,47
ROI1=thresh[b:b+d,a:a+c]
option1= pytesseract.image_to_string(ROI1, lang='eng',config='--psm 6')
option1=option1[:-2]
print(option1)
e,f,g,h=55, 364, 232, 37
ROI2=thresh[f:f+h,e:e+g]
option2=pytesseract.image_to_string(ROI2, lang='eng',config='--psm 6')
option2=option2[:-2]
print(option2)
i,j,k,l=56, 426, 224, 39
ROI3=thresh[j:j+l,i:i+k]
option3=pytesseract.image_to_string(ROI3, lang='eng',config='--psm 6')
option3=option3[:-2]
print(option3)
#cv2.imshow('thresh', thresh)
#a=cv2.imshow('ROI', ROI)
cv2.waitKey()
r=requests.get("http://google.com/search?q="+question[:-1])
#print("http://google.com/search?q="+question)
soup=BeautifulSoup(r.text,'html.parser')

response=soup.find_all("span",class_="st")
res=str(r.text)
#print(response)
#print(res)
countoption1=res.count(option1)
countoption2=res.count(option2)
countoption3=res.count(option3)
print(countoption1,countoption2,countoption3)
maxcount=max(countoption1,countoption2,countoption3)
if countoption1==maxcount:
    print("A")
elif countoption2==maxcount:
    print("B")
else:
    print("C")





