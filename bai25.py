# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 07:01:20 2024

@author: PHAM THU THANH
"""

chu_cai = input("Nhap mot chu cai:")
if chu_cai.islower():
    print("Chu hoa la:",chu_cai.upper())
else:
    print("Chu thuong la:", chu_cai.lower())
    