def Ejercicio3_1(self):
        #   Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene 
        #   dicho número.

        numero=0
        while numero<=0:
            numero=int(input("ingrese un numero: "))

        cont=0
        while numero>0:
            numero//=10
            cont+=1


        print("la cantidad de dijitos que tiene la canatidad es de:",cont)