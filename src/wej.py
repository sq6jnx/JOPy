import numpy as np
import pandas as pd
from Multiplet import Multiplet, line, F
from LevMarJO import LevMar

x = Multiplet()
x.load_file("./Test inputs/ErbLGSO_zdeczkapoprawka.in")

print(x)
"""with open(r"./Test inputs/ErbLGSO_test.in") as f:
     lines = [ line.strip('\n') for line in f ]
np.set_printoptions(precision=3)
names=['f','wavenumber','u2','u4','u6']
fajl=pd.read_csv("ErbLGSO_test.in",sep=" ",header=None,names=names)
print(fajl)
twojplusone=fajl["f"][0]
n=fajl["wavenumber"][0]
dane=[]
for i in range(1,fajl.shape[0]):
#   print (fajl["wavenumber"][i],fajl["u2"][i],fajl["u4"][i],fajl["u6"][i])
   dane.append(list((fajl["f"][i],
                     fajl["wavenumber"][i],
                     fajl["u2"][i],
                     fajl["u4"][i],
                     fajl["u6"][i])))

print (dane)
(twojplusone,n)=lines[0].split(' ')
print (twojplusone,n)
x.n=float(n)
x.tjpo=float(twojplusone)
for i in range(1,len(lines)):
   (f,wn,u2,u4,u6)=lines[i].split(' ')
   x.add_line(line(f,wn,u2,u4,u6))
print (x)
#for line in x.lines:
#    print(F(line, x.n, x.tjpo, 1.0e-20, 1.0e-20, 1.0e-20))"""
params = LevMar(x)
emi = Multiplet()
emi.load_rate("./Test inputs/amd4i13_2.txt")
emi.n = x.n
emi.calculate_rates(params)
"""for line in x.lines:
   ft=F(line,x.n,x.tjpo,params[0],params[1],params[2])
   fexp=line.f
   #print (f"{int(line.wn)} {fexp:.4} {ft:.4} {100*(fexp-ft)/fexp:.4}")
   print(f"{F(line,x.n,x.tjpo,1.234e-20,2.137e-20,3.654e-20)} {line.wn} {line.u2} {line.u4} {line.u6}")
"""
