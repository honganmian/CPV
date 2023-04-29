#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 


# In[3]:


cap = cv2.VideoCapture(0)
print(cap)
while True:
    ret, frame = cap.read()
    if ret == True:
        print("image")
        
    cv2.imshow("Video from Webcam", frame)
    
    if cv2.waitKey(1) & 0xff== ord('q'):
        break
cap.release()
cv.destroyAllWindows()


# In[ ]:




