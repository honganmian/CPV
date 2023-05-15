#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mport cv2 as cv
import numpy as np

def rect(n, m):
    global background
    try:
        n = int(n)
        m = int(m)
        
        if n != 0 and n != 1:
            print("n must be in range[0,1].")
            return
        if n == 1:
            background = np.ones((m, 2*m, 3))
            cv.imshow('White background', background)
            
        else:
            background = np.zeros((m, 2*m, 3))
            cv.imshow('Black background', background)
        
        cv.waitKey(0)
        cv.destroyAllWindows()
        return background
    except ValueError:
        
        print("n is integer")
        
def rect_show():
    n = (input('Enter n: '))
    m = (input('Enter weight and height of the rect: '))
    rect(n,m)

    
rect_show()


# In[ ]:





# In[ ]:




