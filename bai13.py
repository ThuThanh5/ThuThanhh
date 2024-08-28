# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:18:22 2024

@author: PHAM THU THANH
"""

ngay = int(input("Nhap ngay sinh:"))
thang = int(input("Nhap thang sinh:"))
nam = int(input("Nhap nam sinh:"))
print(f"a) {ngay}/{thang}/{nam}")
print(f"b) {ngay}/{thang}/{str(nam)[-2:]}")
print(f"c) {nam}/{thang}/{ngay}")

#Lam nguoc lai:
print(f"a) {nam}/{thang}/{ngay}")
print(f"b) {str(nam)[-2:]}/{thang}/{ngay}")
print(f"c) {ngay}/{thang}/{nam}")

