#codigo principal

cedula=int(input("Digite su cedula sin puntos ni espacios: "))
nombre=str(input("digite su nombre completo: "))
salario_basico=int(input("digite su salario basico: "))
dias_labo=int(input("Digite los dias laborados: "))
ventas=int(input("Digite el valor total de ventas: "))
descuentos=int(input("Digite si tiene prestamos: "))
aux_trans=117112*dias_labo/30
#Llama funcion
def calculadora(cedula,nombre,salario_basico,dias_labo,ventas,descuentos,aux_trans):
    if salario_basico<=2000000:
        salario=salario_basico+aux_trans
        sueldo=salario*dias_labo/30
    else:
        sueldo=salario_basico*dias_labo/30
        print(sueldo)
    comision=ventas*2/100
    total_devengado=sueldo+comision
    salario_neto=total_devengado-descuentos
    print(f"\nCedula empleado:{cedula},\nnombre de empleado:{nombre},\nSalario basico:{salario_basico},\nAuxilio de trasnporte:{aux_trans},\nComision de ventas:{comision},\nDescuentos:{descuentos}")
    print("el salario total es:",salario_neto)

c=calculadora(cedula,nombre,salario_basico,dias_labo,ventas,descuentos,aux_trans)
print(c)
