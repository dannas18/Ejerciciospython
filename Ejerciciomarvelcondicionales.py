puede_volar = input("puede volar si o no;")
es_humano = input("es humano si o no;")
tiene_mascara = input("tiene mascara si o no;")

if puede_volar=="si":
    if es_humano=="si":
        if tiene_mascara=="si":
            print('Ironman')
        else:
            print('Captain Marvel')
    else:
        if tiene_mascara=="si":
            print('Ronan Accuser')
        else:
            print('Vision')
else:
    if es_humano=="si":
        if tiene_mascara=="si":
            print('Spiderman')
        else:
            print('Hulk')
    else:
        if tiene_mascara=="si":
            print('Black Bolt')
        else:
            print('Thanos')