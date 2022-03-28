nif=int(input('introdusca su NIF aqui'))
tabla_de_control='TRWAGMYFPDXBNUZSQVHLCKE'
control_digital=tabla_de_control[nif%23]
whole_nif=str(nif)+control_digital
print(whole_nif)