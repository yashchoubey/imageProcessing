import pylab
import numpy as np
from scipy.misc import imread,imshow

a = imread("pic1.jpg")
b = imread("pic2.jpg")


c = (a+b)/2.0
imshow(c)

print "-----------------------"
max_element=np.amax(c)
min_element=np.amin(c)


c=(c-min_element)/(max_element-min_element)

#print c
#imshow(c)
