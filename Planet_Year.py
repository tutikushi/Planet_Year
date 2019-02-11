# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import pi

r = input("Radius of the orbit: ")
v = input("Orbital speed: ")
r = float(r)
v = float(v)

year = 2*pi*r/v
year = year/(60*60*24)

print(round(year))