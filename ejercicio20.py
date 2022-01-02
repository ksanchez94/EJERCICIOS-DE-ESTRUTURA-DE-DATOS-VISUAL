def Ejercicio2_9(self):
        #   Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho 
        #   número.


        numero=0
        while numero<=0 or numero >=13:
            numero=int(input("ingrese cantidad deseada: "))

        if numero== 1:
            print("Enero")
        elif numero== 2:
            print("febrero")
        elif numero==3:
            print("marzo")
        elif numero==4:
            print("abril")
        elif numero==5:
            print("mayo")
        elif numero==6:
            print("junio")
        elif numero==7:
            print("julio")
        elif numero==8:
            print("agosto")
        elif numero==9:
            print("septiembre")
        elif numero==10:
            print("octubre")
        elif numero==11:
            print("noviembre")
        elif numero==12:
            print("diciembre")
