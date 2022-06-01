lista=[5,10,3,5,1,46,33,6]
cadena=""
coma=","
for i in lista:
    print(i)
cadena+=str(i)+coma
print(cadena)
def contador(lista):
    lista.sort(reverse=True)
    print(lista)
def buscar(lista):
    buscar=input('Digite el valor a buscar: ')
    while lista != "no":
        print(buscar)

print( contador(lista), buscar(lista))