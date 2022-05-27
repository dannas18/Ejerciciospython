lista=["piña","mazana","papaya","fresa","banana","sandia","lulo","mora","kiwi","melon"]
def frutas(lista):
    for i in lista:
        print(i)
print(frutas(lista))
def buscar(lista):
    while lista != 'i':
        print("La letra no es la que busco")
        lista= input('Introduce la letra')
        