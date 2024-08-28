# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 08:19:27 2024

@author: PHAM THU THANH
"""

import math
# Nhập loại hình
hinh = input("Nhập hình (v: vuông, n: chữ nhật, t: tròn): ")

if hinh == 'v':
    canh = float(input("Nhập cạnh của hình vuông: "))
    P = 4 * canh
    S = canh ** 2
    print(f"Chu vi P = {P}, Diện tích S = {S}")

elif hinh == 'n':
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    P = 2 * (dai + rong)
    S = dai * rong
    print(f"Chu vi P = {P}, Diện tích S = {S}")

elif hinh == 't':
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    P = 2 * math.pi * ban_kinh
    S = math.pi * ban_kinh ** 2
    print(f"Chu vi P = {P}, Diện tích S = {S}")

else:
    print("Loại hình không hợp lệ")