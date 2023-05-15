#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv
import numpy as np


class median_filter(object):

    def __init__(self, image, kernel_size):

        self.image = image
        self.kernel_size = kernel_size

        self.H = image.shape[0]
        self.W = image.shape[1]

        self.image_res = image.copy()

    def calculate_median(self, img):
        vector = img.flatten()
        vector = sorted(vector)
        median = int(len(vector) / 2)
        return vector[median]

    def preprocessing_image(self):

        for H in range(self.H):
            H_start = H
            H_end = H_start + self.kernel_size
            for W in range(self.W):
                W_start = W
                W_end = W_start + self.kernel_size

                tmp = self.image[H_start: H_end, W_start: W_end]
                if tmp.shape[0] == self.kernel_size and tmp.shape[1] == self.kernel_size:
                    self.image_res[H_start: H_end, W_start: W_end][int(self.kernel_size / 2)][
                        int(self.kernel_size / 2)] = self.calculate_median(tmp)
                else:
                    break
        return self.image_res


image = cv.imread(r"C:\Users\NGUYEN HONG AN\Downloads\image_noise.jpg", 0)
image = cv.resize(image, (512, 512))

image_median = median_filter(image, 7)
image_median = image_median.preprocessing_image()

cv.imshow("org", image)
cv.imshow("median", image_median)
cv.waitKey(0)


# In[ ]:




