#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 18:13:14 2018

@author: zhaolei
"""
import re
import codecs

def filter_null(c):
    if not re.match('[\\x00\\xff\\xfe]', c):
        return True
    
if __name__ == '__main__':
    try:
        fr=open('./data/email/spam/17.txt' )
        a=fr.read()
    except:
        print ("error")
        fr.close()