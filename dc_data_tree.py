# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:34:50 2017

@author: tkjs2
"""
import numpy as np
import glob
import os
import shutil

# CREATING STRUCTURE
os.mkdir("valid")
os.mkdir("train/dogs")
os.mkdir("train/cats")
os.mkdir("valid/dogs")
os.mkdir("valid/cats")


f_dogs=glob.glob("./train/dog*")
f_cats=glob.glob("./train/cat*")

from sklearn.model_selection import train_test_split

train_dogs, val_dogs = train_test_split(f_dogs, test_size = 0.2)
train_cats, val_cats = train_test_split(f_cats, test_size = 0.2)


## MOVING FILES
for e in train_dogs:
    shutil.move(e,"train/dogs/"+e.replace("./train\\",""))

for e in train_cats:
    shutil.move(e,"train/cats/"+e.replace("./train\\","")) 

for e in val_cats:
    shutil.move(e,"valid/cats/"+e.replace("./train\\",""))

for e in val_dogs:
    shutil.move(e,"valid/dogs/"+e.replace("./train\\","")) 
