#!/usr/bin/env python
# coding: utf-8

# In[23]:


import cv2 as cv
import numpy as np


# In[ ]:



def square(n, m):
    global background
    try:
        n = int(n)
        m = int(m)
        
        if n != 0 and n != 1:
            print("n must be in range[0,1].")
            return
        if n == 1:
            background = np.ones((m, m, 3))
            cv.imshow('White background', background)
            
        else:
            background = np.zeros((m, m, 3))
            cv.imshow('Black background', background)
        
        cv.waitKey(0)
        cv.destroyAllWindows()
        return background
    except ValueError:
        
        print("n is integer")
        
def square_show():
    n = (input('Enter n: '))
    m = (input('Enter weight and height of the square: '))
    square(n,m)

    
square_show()


# In[ ]:





# In[ ]:





# In[ ]:




