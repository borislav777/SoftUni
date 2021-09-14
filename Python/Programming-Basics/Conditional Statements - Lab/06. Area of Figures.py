from math import pow
from math import pi


type=input()
if type=='square':
    a=float(input())
    square_area=pow(a,2)
    print(f"{square_area:.3f}")
elif type=='rectangle':
    a=float(input())
    b=float(input())
    rectangle_area=a*b
    print(f"{rectangle_area:.3f}")
elif type=='circle':
    r=float(input())
    circle_area=pi*pow(r,2)
    print(f"{circle_area:.3f}")
elif type=='triangle':
    a=float(input())
    h=float(input())
    triangle_area=a*h/2
    print(f"{triangle_area:.3f}")


