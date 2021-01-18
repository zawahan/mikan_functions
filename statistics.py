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


# img をもとに統計量を出す．

def statis(img, imgname):
    
    sr_img = pd.Series(np.ravel(img))
    df_img = pd.DataFrame(sr_img.describe(),columns= [imgname])
    
    return df_img

# img(ndarray)のlistをもとに統計量を出す．

def statis_list(masked_VIimg_list):
    
    statis_list = []
    c = 0
    for img in masked_VIimg_list:
        sr_img = pd.Series(np.ravel(img))
        df_img = pd.DataFrame(sr_img.describe(),columns= [str(c)])
        statis_list.append(df_img)
        c += 1
        
    return statis_list

