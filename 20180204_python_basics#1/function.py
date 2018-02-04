#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check(height):
    if height >= 160:
        return "John"
    else:
        return "Michel"

name = "who"
print(name)
h = 170
name = check(h)
print(name)
