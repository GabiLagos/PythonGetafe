print("Practica Horas Extra")
print("Ingrese las horas trabajadas")
horas = int(input())
print("Ingrese el precio hora")
preciohora = int(input())
print("Ingrese los kilometros recorridos")
kms = int(input())

if (kms<100):
    print("Sus dietas son LOCALES")
elif (kms<500 and kms>=100):
    print("Sus dietas son PROVINCIALES")
else:
    print("Sus dietas son NACIONALES")

if (horas>=36):
    sal_base = 36 * preciohora
    sal_extra = (horas - 36) * (preciohora + 2)
    sal_total = sal_extra + sal_base
else:
    sal_base = horas * preciohora
    sal_extra = 0
    sal_total = sal_extra + sal_base
print ("Su salario base es ", sal_base, "€")    
print ("No ha hecho horas extra")
print ("Su salario total es ", sal_total, "€")
    
if (sal_total<=250):
    print ("Ud. no tiene retenciones")
elif (sal_total>250 and sal_total<=600):
    print ("Sus retenciones son de 20%")
elif (sal_total>600):
    print("Sus retenciones son de 40%")
    
print("Fin de la practica")
