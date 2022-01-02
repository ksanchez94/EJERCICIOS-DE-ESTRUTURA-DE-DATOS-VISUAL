def Ejercicio2_2(self):
        #   Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es 
        #   capicúa.
        #   Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.


        numero=0
        while numero<=0:
            numero=int(input("ingrese un numero de 5 dijitos: "))
        a=str(numero)
        if a[0] == a[4] and a[1] == a[3]:
            print("Si es capicúa.")
        else:
            print("No es capicúa ")