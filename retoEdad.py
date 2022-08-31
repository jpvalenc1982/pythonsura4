edad=int(input("Digite su edad: "))
#mes=mesent.lower()
#PROCESO
if(edad>=0 and edad<14):
    #SALIDA
    print(f'La persona tiene {edad} años y es niño')
elif(edad>=14 and edad<28):
    #SALIDA
    print(f'La persona tiene {edad} años y es joven')
elif(edad>=28 and edad<60):
#SALIDA
    print(f'La persona tiene {edad} años y es adulto')  
elif(edad>=100):
    #SALIDA
    print(f'La persona tiene {edad} años y es adulto mayor')
else:
    print(f'La edad no es válida')