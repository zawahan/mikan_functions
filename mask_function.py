#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set()
import os

import cv2


# In[ ]:


# masklistを返す
# masklist 0番目はオリジナルのマスク,1番目以降は穴（マスクオブジェクト）一つ一つを分けたマスク
# masklistの各要素は bool indexになっている．

def make_masklist(maskimg):

    nlabel, img_lab = cv2.connectedComponents(maskimg)

    masklist = [(maskimg == 255)]
    for n in range(1,nlabel,1):
        mask_n = (img_lab == n)
        masklist.append(mask_n)

    return masklist


# In[ ]:


# 一枚のVIimgに対して，複数のマスクを適用して，リストにして返す．

def masked_VIimg(masklist, VIimg):

    for_graph  = []
    for_statis = []
    for mask in masklist:
        mm_for_graph  = VIimg * mask
        mm_for_statis = VIimg[mask]
        for_graph.append(mm_for_graph)
        for_statis.append(mm_for_statis)

    return for_graph, for_statis
