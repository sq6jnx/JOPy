rho=4.26
Ge=72.612759
O= 15.999405
Te=127.603125
Sr=87.616646
F=18.998403
Dy=162.497030
GTS4=46*(Ge+2*0)+35*(Te+2*O)+15*(Sr+2*F)+4*(2*Dy+3*O)#mol zwiazku
print ("Masa molowa ",GTS4)
mmol=GTS4
molinalitr=1000*rho/mmol
print("Moli na litr ",molinalitr )
print (molinalitr*8)
print (6.02214129e23*molinalitr*(8)/1000)