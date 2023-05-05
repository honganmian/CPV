#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2 as cv
import numpy as np


# In[11]:


background = np.ones((255, 255))
cv.imshow('White background', background)
cv.waitKey(0)
cv.destroyAllWindows()


# In[ ]:




