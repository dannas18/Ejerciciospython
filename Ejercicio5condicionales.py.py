edad = int (input("introduzca su edad "))
peso = int (input("introduzca su peso "))
pulso = int(input("introduzca su pulso "))
plaquetas = int(input("introduzca numero de plaquetas "))

if edad >= 18 <= 65:
    if peso >= 50:
        if pulso >= 50 <= 110:
            if plaquetas >= 150000:
                print("apto para donar sangre")
            else:
                print("no apto para donar sangre")
        else:
            print("no es apto para donar sangre")
    else:
         print("no es apto para donar sangre")
else:
     print("no es apto para donar sangre")