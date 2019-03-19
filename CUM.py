# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 21:24:53 2018

@author: Carl
"""

import cv2
import sys
from numpy import *
import numpy as np
image = cv2.imread('D:/rose.png') # 根據路徑選取一張照片
#image=cv2.resize(imagein,(512,512))
reflect_img = cv2.copyMakeBorder(image,1,1,1,1,cv2.BORDER_REPLICATE)#填充边界像素
x,y=reflect_img.shape[:2]
for depth in range(0,3):
    for rows in range(1,x-1):
        for colums in range(1,y-1):
            CUM = pow(reflect_img.item(rows-1,colums,depth)-reflect_img.item(rows+1,colums,depth),2)\
            *(reflect_img.item(rows,colums,depth)*2-reflect_img.item(rows-1,colums,depth)-reflect_img.item(rows+1,colums,depth))\
            +pow(reflect_img.item(rows,colums-1,depth)-reflect_img.item(rows,colums+1,depth),2)\
            *(reflect_img.item(rows,colums,depth)*2-reflect_img.item(rows,colums-1,depth)-reflect_img.item(rows,colums+1,depth))
 
            Value = reflect_img.item(rows-1,colums-1,depth)+0.002*CUM
            if(Value > 255):
                Value = 255
            elif(Value < 0):
                Value = 0
            reflect_img.itemset((rows-1,colums-1,depth),Value)
#####################################################################
cv2.imshow("reFlect image",reflect_img)
cv2.namedWindow("Image") # 初始化一个名为Image的窗口
cv2.imshow("Image", image) # 显示图片
cv2.imwrite("D:/revolution1.jpg",image)
cv2.waitKey(0) # 等待键盘触发事件，释放窗口
