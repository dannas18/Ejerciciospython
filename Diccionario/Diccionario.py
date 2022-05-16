from ast import operator
from optparse import AmbiguousOptionError

import operator


diccionario= dict(
    Enero=30, 
    Febrero=23,
    Marzo=21,
    Abril=12,
    Mayo=21,
    Junio=55,
    Julio=31,
    Agosto=45,
    Septiembre=33,
    Octubre=22,
    Noviembre=56,
    Diciembre=60
)

max_key= max(diccionario.items(), key=operator.itemgetter(1))[0]
print(max_key)

min_key= min(diccionario.items(), key=operator.itemgetter(1))[0]
print(min_key)

a=tuple(diccionario.values())
b=len(a)
sum=0
for val in a:
    sum+=val
print("promedio", sum/b)

for key in diccionario.keys():
    if (diccionario[key]>=val):
        print("el mes",key,"es mayor que el promedio")
    
    elif (diccionario[key]<=val):
        print(f"el mes:{key}, es menor que el promedio")



