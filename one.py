import pytesseract as ress
import cv2
from PIL import Image, ImageFont, ImageDraw
class Output:
    BYTES = 'bytes'
    DATAFRAME = 'data.frame'
    DICT = 'dict'
    STRING = 'string'
class Data:
    x=0
    y=0
    w=0
    h=0
    text=''
list_f = ['[name]','[phoneNumber]','[address]','[date]']
list_g =[]
img = cv2.imread('template.png')
text = ress.image_to_data(img,output_type=Output.DICT)
f=0
for i in text["text"]:
    if(i in list_f):
        print(i)
        data =Data()
        data.x = text["left"][f]
        data.y = text["top"][f]
        data.w = text["width"][f]
        data.h = text["height"][f]
        data.text = text["text"][f]
        list_g.append(data)
    f+=1
for data in list_g:
    start_point = (data.x+2, data.y)
    end_point =(data.x+data.w, data.y+data.h)
    thickness = -1
    color =(255,255,255)
    image = cv2.rectangle(img, start_point, end_point, color, thickness) 
    color = (0,0,0)
    thickness =1
    font = cv2.FONT_HERSHEY_TRIPLEX
    org =  (data.x+2, data.y+data.h)
    fontScale = 1
    image = cv2.putText(img, '', org, font,  fontScale, color, thickness)
cv2.imwrite("output.png", img)
