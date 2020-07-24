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
img = Image.open(r'template.png') 
draw = ImageDraw.Draw(img)
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
    shape = [(data.x+2,data.y), (data.x+data.w,data.y+data.h)] 
    draw.rectangle(shape, fill ="#FFFFFF",outline='red')
    org =  (data.x+5, data.y-2)
    font = ImageFont.truetype(r'arial.ttf', 20)
    draw.text(org, 'text', fill ="black",font= font, align ="left")
img =img.save("output.png")
