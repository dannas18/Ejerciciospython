lista=("Danna","Alejandro","Andrea","Alvaro","Daniel","Alejandra","Huber","Sebastian","Lina","Laura")
def recorrido(lista):
    for i in lista:
     print(i)
print(recorrido(lista))
#def orden(lista):
 #   lista.sort(reverse=True)
  #  print(f"{lista}")
#print(orden(lista))
def buscar(lista):
    while lista != 'a':
        print('La letra no es la que busco')
        lista = input('introduce una letra ')
    print ('la letra es a, por eso salgo del bucle')
print(buscar(lista))
def longitud(lista):
    c=len(lista)
    print(c)
print(longitud(lista))