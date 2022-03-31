samba_ruta='1.1.1.1/eoi/python'
samba_ruta=samba_ruta[2:]
posicion_barra=samba_ruta.index('/')
hots= samba_ruta[:posicion_barra]
path=samba_ruta[posicion_barra:]
print(f'host={hots}); path={path}')