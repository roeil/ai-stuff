# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:53:55 2020

@author: roy
"""

import os
import numpy as np
import pandas as pd

os.chdir("C:\\Users\\roy\\Desktop\\brian ai\\language\\parser")

print(os.listdir())


s=[]
s1=[]
for f in os.listdir("sentences"):
    f1=open("sentences/"+f)
    s.append(f1.read())
    s1.append(pd.read_csv("sentences/"+f))
s2=[s[i][:len(s[i])-2] for i in range(len(s))]


term={"Adj": ["country" , "dreadful" , "enigmatical" , "little" , "moist", "red",\
 "down" , "here" , "never"],
"Conj":[ "and" , "until"],
"Det":[ "a" , "an" , "his" , "my" , "the"],
"N": ["armchair" , "companion" , "day" , "door" , "hand" , "he" , "himself", \
"holmes" , "home" , "i" , "mess" , "paint" , "palm" , "pipe" , "she", \
      "smile" , "thursday" , "walk" , "we" , "word"],

"P":[ "at" , "before" , "in" , "of" , "on" , "to"],
"V":[ "arrived" , "came" , "chuckled" , "had" , "lit" , "said" , "sat",\
     "smiled" , "tell" , "were"]}


ss2=[]

for sen in s2:
    sp=sen.split(" ")
    ln=len(sp)
    ss=[]
    for j in range(ln):
        
        print (sp[j].lower())
        for item in term.items():
            
        #    print(value)
            if sp[j].lower() in item[1]:
                print(item[0])
                ss.append(item[0])
    ss2.append(ss)
        