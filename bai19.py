# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:52:04 2024

@author: PHAM THU THANH
"""

a = int(input("Nhap so nguyen a:"))
b = int(input("Nhap so nguyen b:"))
c = int(input("Nhap so nguyen c:"))
d = int(input("Nhap so nguyen d:"))
#Gia su a la so nho nhat
so_nho_nhat = a
if b < so_nho_nhat:
    so_nho_nhat = b
if c < so_nho_nhat:
    so_nho_nhat = c
if d < so_nho_nhat:
    so_nho_nhat = d
print("So nho nhat la:", so_nho_nhat)
            