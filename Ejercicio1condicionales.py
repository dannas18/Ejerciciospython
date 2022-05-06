print("juega piedra, papel o tigera")
print(" ")
persona1= input("persona1 cual elige:")
print(" ")
persona2= input("persona2 cual elige:")

if persona1 ==  persona2:
    msg = 'Empate'
    winner = 0
elif persona1 == 'piedra' and persona2 == 'tijera':
    msg = 'La piedra aplasta la tijera'
    winner = 1
elif persona1 == 'tijera' and persona2 == 'piedra':
    msg = 'La piedra aplasta la tijera'
    winner = 2
elif persona1 == 'tijera' and persona2 == 'papel':
    msg = 'La tijera corta el papel'
    winner = 1
elif persona1 == 'papel' and persona2 == 'tijera':
    msg = 'La tijera corta el papel'
    winner = 2
elif persona1 == 'papel' and persona2 == 'piedra':
    msg = 'El papel envuelve la piedra'
    winner = 1
elif persona1 == 'piedra' and persona2 == 'papel':
    msg = 'El papel envuelve la piedra'
    winner = 2

if winner == 0:
    msg = 'Empate'
else:
    msg = f'Gana persona{winner}: {msg}'

print(msg)
