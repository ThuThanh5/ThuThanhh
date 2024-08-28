# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:06:15 2024

@author: Student
"""

N = int(input("Nhap so nguyen duong N:"))
if N >= 10 and N <= 99:
    hangdonvi = N%10
    hangchuc = N//10
    tong = hangdonvi + hangchuc
    print("Tong cac chu so cua N la:", tong)
    