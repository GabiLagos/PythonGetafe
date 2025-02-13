provincias = dict()
provincias = {
    924 : "Badajoz",
    956 : "Cádiz",
    958 : "Granada",
    959 : "Huelva",
    91 : "Madrid",
    95 : "Málaga",
    968 : "Murcia",
    923 : "Salamanca",
    95 : "Sevilla",
    922 : "Sta. Cruz de Tenerife",
    975 : "Soria",
    96 : "Valencia",
    976 : "Zaragoza"}
print(provincias)
#listar los pare clave, valor de un diccionario
print("Listar los pare clave, valor de un diccionario")
for clave,valor in provincias.items():
    print("Prefijo: ", clave,"Provincia: ",valor)
    
print("================================================================")

print("Número de provincias:",len(provincias))
print("================================================================")
for claves in provincias.keys():
    print ("Prefijo:", claves)
print("================================================================")
for prov in provincias.values():
    print ("Provincia:", prov)
print("================================================================")
#Insertar un elemento en el diccionario
provincias.setdefault(925, "Toledo")
for clave,valor in provincias.items():
    print("Prefijo: ", clave,"Provincia: ",valor)
print("Hemos metido a Badajoz")
print("================================================================")
#Eliminar un elemento del diccionario
provincias.pop (924)
for clave,valor in provincias.items():
    print("Prefijo: ", clave,"Provincia: ",valor)
print ("Ya no esta Badajoz")
print("================================================================")
