#! /usr/bin/python
# coding utf8
from random import randint
x=0
c=0
while x != 3:
    x = randint (1,6)
    print(x)
    c=c+1
print("Contador", c)
print(x)

