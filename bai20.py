# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:01:31 2024

@author: PHAM THU THANH
"""

a = int(input("Nhap so nguyen a:"))
b = int(input("Nhap so nguyen b:"))
c = int(input("Nhap so nguyen c:"))
#Gia su a la so lon nhat
max = a
if b > max:
    max = b
if c > max:
    max = c
print("So lon nhat la:", max)
