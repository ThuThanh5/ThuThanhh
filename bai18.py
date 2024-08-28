# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:36:10 2024

@author: PHAM THU THANH
"""
#Doi thanh giay
def doi_thanh_giay(gio,phut,giay):
    return gio*3600 + phut*60 + giay
#Nhap gio 1
gio1=int(input("Nhap gio 1:"))
phut1=int(input("Nhap phut 1:"))
giay1=int(input("Nhap giay :"))
#Nhap gio 2
gio2=int(input("Nhap gio 2:"))
phut2=int(input("Nhap phut 2:"))
giay2=int(input("Nhap giay 2:"))
tong_giay_1 = doi_thanh_giay(gio1, phut1, giay1)
tong_giay_2 = doi_thanh_giay(gio2,phut2,giay2)
#Tinh tong va hieu
Tong_giay = tong_giay_1 + tong_giay_2
Hieu_giay = tong_giay_1 - tong_giay_2
print("Tong cua 2 gio la:", Tong_giay)
print("Hieu cua 2 gio la:", Hieu_giay)
