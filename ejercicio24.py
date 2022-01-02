def Ejercicio3_2(self):
        #   Dado un número, determine si es capicúa.
        #   Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.


        numero=0
        while numero<=0:
            numero=int(input("ingrese un numero: "))
        a=str(numero)
        contador=0

        while numero>0:
            numero//=10
            contador+=1

        if contador==2:
            if a[0] == a[1]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==3:
            if a[0] == a[2]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==4:
            if a[0] == a[3] and a[1] == a[2]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==5:
            if a[0] == a[4] and a[1] == a[3]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==6:
            if a[0] == a[5] and a[1] == a[4] and a[2] == a[3] :
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==7:
            if a[0] == a[6] and a[1] == a[5] and a[2] == a[4]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")
        elif contador==8:
            if a[0] == a[7] and a[1] == a[6] and a[2] == a[5] and a[3] == a[4]:
                print("Si es capicúa.")
            else:
                print("No es capicúa ")