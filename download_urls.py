#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 20:36:39 2022

@author: ahmed elsherbini
"""
#ref:https://medium.com/@petehouston/download-files-with-progress-in-python-96f14f6417a2
#ref:https://www.programcreek.com/python/example/83386/wget.download
#################################
import wget
import pandas as pd
import argparse
import os
from urllib.parse import urlparse
#################################
#def bar_custom(current, total, width=80):
# print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))
#################################
#step1
my_parser = argparse.ArgumentParser(description='Make sure your files exsit in the data folder!')
#################################
#step2
my_parser.add_argument('-i','--input',
                       action='store',
                       metavar='input',
                       type=str,
                       help='the path to your file')
##################################################
#step3
args = my_parser.parse_args()
##################################################
#step4
f_name = args.input

##################################################
#step5 the analysis 
manifest_df = pd.read_csv("example.tsv", sep='\t')

list_of_single_column = manifest_df['urls'].tolist()
cc=0
for x in list_of_single_column:
    try:
     a = urlparse(x)
     cc +=1    
     print("File number %d" %int(cc))    
     print(os.path.basename(a.path))
     wget.download(x)
    except:
       print("Erorr in file %s"%(os.path.basename(a.path)))
else:
  print("Finally finished!") 

    #os.system(f"""wget -c --read-timeout=5 --tries=0 "{x}"""")
##################################################
   
