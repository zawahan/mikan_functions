#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set()
import os

import cv2


# In[ ]:


# 以下のように読み込む予定
"""
color2gray = cv2.imread(p[0],0)
color      = cv2.imread(p[1])
mask       = cv2.imread(p[2],0)
B          = cv2.imread(p[3],0) 
G          = cv2.imread(p[4],0) 
R          = cv2.imread(p[5],0) 
REDEDGE    = cv2.imread(p[6],0) 
NIR        = cv2.imread(p[7],0) 
"""

# また，引数には，0~1の範囲に正規化したndarrayを入れること．


# In[ ]:


# DVI = NIR - RED

def DVI(red, nir):
    dvi = nir - red
    return dvi


# In[ ]:


# GI = GREEN/RED

def GI(green, red):
    gi = green/red
    return gi


# In[ ]:


# MSAVI = 2NIR+1-( √2(NIR+1)^2 -√8(NIR-RED) )/2

def MSAVI(red, nir):
    msavi = 2*nir+1-( np.sqrt(2)*(nir+1)**2-np.sqrt(8)*(nir-red) )/2
    return msavi


# In[ ]:


# NDVI = (NIR-RED)/(NIR+RED)

def NDVI(red, nir):
    ndvi = (nir-red)/(nir+red)
    return ndvi


# In[ ]:


# NDGI = (NIR-GREEN)/(NIR+GREEN)

def NDGI(green, nir):
    ndgi = (nir-green)/(nir+green)
    return ndgi


# In[ ]:


# NDRE = (NIR-REG)/(NIR+REG)
# REG = red edge　のことらしい．元論文で，720nmくらいとかいてある．NIR は790nmとかいてある．
def NDRE(reg, nir):
    ndre = (nir-reg)/(nir+reg)
    return ndre


# In[ ]:


# OSAVI = (NIR-RED)/(NIR+RED+0.16)

def OSAVI(red, nir):
    osavi = (nir-red)/(nir+red+0.16)
    return osavi


# In[ ]:


# RGRI = RED/GREEN

def RGRI(green, red):
    rgri = red/green
    return rgri


# In[ ]:


# RDVI = (NIR-RED)/(NIR+RED)**(1/2)

def RDVI(red, nir):
    rdvi = (nir-red)/np.sqrt(nir+red)
    return rdvi


# In[ ]:


# SR = NIR/RED

def SR(red, nir):
    sr = nir/red
    return sr


# In[ ]:




