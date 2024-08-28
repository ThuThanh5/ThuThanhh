# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:32:12 2024

@author: PHAM THU THANH
"""

so1 = int(input("Nhap so thu nhat:"))
so2 = int(input("Nhap so thu hai:"))
so3 = int(input("Nhap so thu ba:"))
so_lon_nhat = max(so1,so2,so3)
so_nho_nhat = min(so1,so2,so3)
print(f"So lon nhat la: {so_lon_nhat}")
print(f"So nho nhat la:{so_nho_nhat}")
