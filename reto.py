#ENTRADAS=VARIABLES=REFERENCIAS EN MEMORIA
#SIEMPRE QUE VOY A PEDIR UN NÚMERO LO ABRAZO CON LA PROPIEDAD, EN ESTE CASO, CON UN ENTERO O FLOAT PARA QUE ME LEA LOS DATOS
edad=float(input("Digite el nivel de agua: "))

#PROCESO
if(edad>=0 and edad<20):
    #SALIDA
    print(f'El nivel de agua es {edad} y este es bajo')
elif(edad>=20 and edad<400):
    #SALIDA
    print(f'El nivel de agua es {edad} operando normalmente')  
elif(edad>=400):
    #SALIDA
    print(f'El nivel de agua es {edad} llamen a FICO Y A LUPE')
else:
    print("El nivel de agua no es válido")