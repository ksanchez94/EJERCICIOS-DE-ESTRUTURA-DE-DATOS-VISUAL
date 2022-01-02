def Ejercicio3_8(self):
        #   Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla 
        #   del 1 hasta la del 10.


        numero=0
        while numero<=0 or numero>=11:
            numero=int(input("ingrese la tabla que desea imprimir:"))

        for i in range(0,13):
            suma= i * numero
            print(numero,"X",i,"=",suma)