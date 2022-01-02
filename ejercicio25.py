 def Ejercicio3_3(self):
        #   Dado un número N determinar si es un número primo.
        #       Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo. 

        numero=0
        while numero<=0:
            numero=int(input("ingrese un numero: "))
        contador=0

        for i in range(2,numero):
            resta=numero%i
            if resta==0:
                contador+=1

        if contador==0:
            print("el",numero, "si es primo.")
        else:
            print("el",numero, "no es primo.")