import string


mesent=input("Digite el mes actual: ")
mes=mesent.lower()
#PROCESO
if(mes=='enero' or mes=='febrero' or mes=='marzo'):
    #SALIDA
    print(f'El estacion es {mes} y es invierno')
elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    #SALIDA
    print(f'El estacion es {mes} y es primavera')
elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    #SALIDA
    print(f'El estacion es {mes} y es verano')
elif(mes=='octubre' or mes=='noviembre' or mes=='diciembre'):
    #SALIDA
    print(f'El estacion es {mes} y es otoño')
else:
    print("Mes inválido")