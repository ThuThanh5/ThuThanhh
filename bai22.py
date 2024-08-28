# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:16:27 2024

@author: PHAM THU THANH
"""

#In phuong trinh bac nhat
a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
print("Phuong trinh bac nhat: {0}X + {1} = 0".format(a,b))
if a!=0:
    x = -b/a
    print("x=", x)
elif b==0:
        print ("phương trình VSN")
else:
            print("phương trình VN")