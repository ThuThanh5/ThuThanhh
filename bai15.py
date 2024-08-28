# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:35:20 2024

@author: PHAM THU THANH
"""

a = float(input("Nhap gia tri a:"))
b = float(input("Nhap gia tri b:"))
a1 = (a**1/3) + (b**1/3)
a2 = (a*b)**1/3
a3 = ((a**1/3)-(b**1/3))**2
b1 = ((a+b)/a1)-a2
BT = b1/a3
print("Gia tri cua bieu thuc la:", BT)