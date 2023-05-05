#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2 as cv
import numpy as np


# In[7]:


image = np.zeros((1000, 1000))
draw = False
x1 = y1 = -1

def Func2(image): 
    def draw_a_rectangle(event, x, y, flags, param):
        global draw, x1, y1
        if event == cv.EVENT_LBUTTONDOWN:
            x1 = x
            y1 = y
            draw = True
        elif event == cv.EVENT_MOUSEMOVE and draw == True:
            cv.rectangle(image, (x1, y1), (x, y), (255, 255, 255), -1)
        elif event == cv.EVENT_LBUTTONUP and draw == True:
            draw = False
            cv.rectangle(image, (x1, y1), (x, y), (255, 255, 255), -1)
        elif event == cv.EVENT_MOUSEMOVE and draw == False:
            print("Di chuyên tìm vị trí vẽ!")
    cv.namedWindow("Draw")
    cv.setMouseCallback("Draw", draw_a_rectangle)
    
    while True:

        cv.imshow("Draw", image)
        if cv.waitKey(1) & 0xff == ord('d'):
            break
    cv.destroyAllWindows()

Function2(image)


# In[ ]:




