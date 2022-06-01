lista=["piña","mazana","papaya","fresa","banana","sandia","lulo","mora","kiwi","melon"]
def frutas(lista):
    for i in lista:
        print(i)
print(frutas(lista))

def valores(lista):
    for i in lista:
     print(i)
print(valores(lista))

def orden(lista):
    lista.sort(reverse=True)
    print(f"{lista}")
print(orden(lista))

def buscar(lista):
    while lista != 'i':
        print("La letra no es la que busco")
        lista= input('Introduce la letra')
        print ('la letra es a, por eso salgo del bucle')
print(buscar(lista))

def longitud(lista):
    c=len(lista)
    print(c)
print(longitud(lista))

        