#ENTRADAS=VARIABLES=REFERENCIAS EN MEMORIA
#SIEMPRE QUE VOY A PEDIR UN NÚMERO LO ABRAZO CON LA PROPIEDAD, EN ESTE CASO, CON UN ENTERO O FLOAT PARA QUE ME LEA LOS DATOS
nivelAgua=float(input("Digite el nivel de agua: "))

#PROCESO
if(nivelAgua>=0 and nivelAgua<20):
    #SALIDA
    print(f'El nivel de agua es {nivelAgua} y este es bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    #SALIDA
    print(f'El nivel de agua es {nivelAgua} operando normalmente')  
elif(nivelAgua>=400):
    #SALIDA
    print(f'El nivel de agua es {nivelAgua} llamen a FICO Y A LUPE')
else:
    print("El nivel de agua no es válido")