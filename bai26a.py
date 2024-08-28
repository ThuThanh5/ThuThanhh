# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 07:53:32 2024

@author: PHAM THU THANH
"""

a = int(input("Nhap so a:"))
b = int(input("Nhap so b:"))
c = int(input("Nhap so c:"))
if a > b:
    a,b = b,a
if a > c:
   a,c = c,a
if b > c:
   b,c = c,b
print(f"So theo thu tu tang dan la:{a},{b},{c}")



        