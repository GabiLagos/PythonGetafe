from class32tempmes import TempMes
import random
mes1 = TempMes()
mes1.nombre="Enero"
mes1.tmax = -5
mes1.tmin = 14

#quiero que las temperaturas salgan del programa, vamos a automatizar las temperaturas
#vamos a usar la clase random que genera números aleatorios decimales o enteros
#primero imprtamos la clase (arriba al comienzo del programa)
mes2 = TempMes()
mes2.nombre="Febrero"
mes2.tmax = random.randint(10,20)
mes2.tmin = random.randint(-5,6) 


#vamos a generar tambien el mes de forma aleatoria usando una tupla


print (mes1)
media = mes1.gettempMedia()
print("La temperatura media en el mes de", mes1.nombre, "fué de",mes1.gettempMedia() ,"ºC")

print (mes1)
media = mes1.gettempMedia()
print("La temperatura media en el mes de", mes1.nombre, "fué de", media,"ºC")
print("La temperatura media en el mes de", mes1.nombre, "fué de", mes1.gettempMedia(),"ºC")
print("===============================================================================")
print (mes2)
media = mes2.gettempMedia()
print("La temperatura media en el mes de", mes2.nombre, "fué de", media,"ºC")
print("_______________________________________________________________________________")
print("                                                                                ")

#ahora quiero que lo haga para todos los meses
meses =("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "dicimebre")
tmax=0
tmin=0

for nombreMes in meses:
    tmax = random.randint(10,20)
    tmin = random.randint(-5,6) 
    print("La temperatura máxima en el mes de",nombreMes,"fué de",tmax ,"ºC, ", "la mínima fué de",tmin ,"ºC y la media fué de", (tmax+tmin)/2)
