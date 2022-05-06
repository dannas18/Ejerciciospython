print("Digite un numero para calcular el minimo")
valor1=int(input("primer número"))
valor2=int(input("segundo número"))
valor3=int(input("tercer número"))

if valor1 < valor2:
    if valor1 < valor3:
        minimo_valor1=valor1
    else:
     minimo_valor= valor3

elif valor2 < valor3:
    minimo_valor= valor2
else:
    minimo_valor=valor3

print("El numero minimo es:", minimo_valor)
