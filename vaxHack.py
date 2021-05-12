#!/usr/bin/env python
# coding: utf-8

# In[67]:


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
import time
from datetime import datetime
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# In[68]:
LOC = "724 325"

def watchMan(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            buff = img[i,j]
            c=0
            if buff[0]==169:
                c+=1
            if buff[1]==209:
                c+=1
            if buff[2]==142:
                c+=1

            if c==3:
                return True
    return False
while(1):
    for PIN in ["382481","380061"]:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        TIME = datetime.fromtimestamp(time.time()).strftime('%HH-%MM : %d-%m-%Y')
        print("TIME:",TIME)
        NAME = f"{time.time()}.png"
        os.system("xdotool mousemove 263 327 click 1")
        os.system("xdotool key ctrl+a")
        for i in PIN:
            os.system(f"xdotool key {i}")
        os.system(f"xdotool mousemove {LOC} click 1")
        time.sleep(1)
        os.system("xdotool mousemove 267 357 click 1")
        time.sleep(1)
        os.system(f"scrot {NAME}")

        #img = mpimg.imread(NAME)
        img = Image.open(NAME)
        width, height = img.size
        TEXT = pytesseract.image_to_string(img)

        if "Signln for Vaccination" in TEXT:
            os.system(f"rm {NAME}")
            from pushbullet import Pushbullet
            APIKEY = "<YOU API KEY OF PUSHBULLETS>"
            pb = Pushbullet(APIKEY)
            push = pb.push_note("LOGOUT!", "Please Login!")
            os.system("xdotool mousemove 598 364 click 1")
            PHNUM = "<Your Phone Number>"
            for i in PHNUM:
                os.system(f"xdotool key {i}")
            os.system("xdotool mousemove 679 403 click 1")
            time.sleep(3)
            while(1):
                if "OTP.txt" in os.listdir():
                    f = open("OTP.txt")
                    OTP = f.read()
                    f.close()
                    os.system("xdotool mousemove 687 357 click 1")
                    for j in OTP:
                        os.system(f"xdotool key {j}")
                    os.system("rm OTP.txt")
                    os.system("xdotool mousemove 682 418 click 1")
                    break
                else:
                    time.sleep(5)
            time.sleep(5)
            os.system("xdotool mousemove 1069 387 click 1")
            time.sleep(2)
            os.system("xdotool mousemove 1049 684 click 1")
            time.sleep(2)
            os.system("xdotool mousemove 425 330 click 1")
            time.sleep(2)
            for i in "382481":
                os.system(f"xdotool key {i}")
            TIME = datetime.fromtimestamp(time.time()).strftime('%HH-%MM : %d-%m-%Y')
            print("TIME:",TIME)
            NAME = f"{time.time()}.png"
            os.system(f"xdotool mousemove {LOC} click 1")
            time.sleep(1)
            os.system("xdotool mousemove 267 357 click 1")
            time.sleep(1)
            os.system(f"scrot {NAME}")
            img = Image.open(NAME)

        img = img.resize((width//2, height//2))
        img = np.array(img)
        #img = mpimg.imread(NAME)

        FLEG = watchMan(img)
        if FLEG:
            print("YAY!")
            from pushbullet import Pushbullet
            APIKEY = "<YOU API KEY OF PUSHBULLETS>"
            pb = Pushbullet(APIKEY)
            push = pb.push_note("Vaccine Available!", f"{TIME}")
        else:
            print("WAAK!")
        os.system(f"rm {NAME}")
