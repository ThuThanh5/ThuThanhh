# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 06:49:44 2024

@author: PHAM THU THANH
"""

gio = int(input("Nhap gio:"))
phut = int(input("Nhap phut:"))
giay = int(input("Nhap giay:"))
if 0 <= gio < 24 and 0 <= phut < 60 and 0 <= giay < 60:
    print("Thoi gian hop le")
else:
    print("Thoi gian khong hop le")
    