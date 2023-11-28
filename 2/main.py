from math import exp, sin, fabs

file = open('input.txt', "r") 
l = open("output.txt", "w") 
a = file.read().split(" ") 
b = list(map(float, a))

def calc(x, y): 
    s = (x**2 + (x+1)**(1/3) / y**3 + 3.23) 
    r = 2.45 * s**2 + s 
    return [x, s, r] 

f = calc(b[0], b[1]) 
l.write(f"{f[0]} {f[1]} {f[2]}")
file.close() 
l.close()