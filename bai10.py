# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:51:53 2024

@author: Student
"""

so_xe = int(input("Nhap bien so xe (gom 4 chu so):"))
nghin = so_xe // 1000
tram = so_xe // 100 % 10
chuc = so_xe // 10 % 10
don_vi = so_xe % 10
nut = nghin + tram + chuc + don_vi
a = nut // 10
b = nut % 10
x = a+b
c = x // 10
d = x % 10
y = c+d
print(f"Bien so xe cua ban duoc {y} nut")
1320