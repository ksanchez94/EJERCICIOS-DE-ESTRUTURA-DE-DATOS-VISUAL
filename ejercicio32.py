def Ejercicio3_10(self):
        #Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que 
        #la serie termina al leer un 0.

        numero = 1
        total = 0
        contador = 0
        lista = ["Ingrese", "Error, Ingrese"]
        posicion = 0
        while numero != 0:
            numero = int(input(lista[posicion] + " un número positivo: "))
            if numero>1:
                posicion = 0
                total += numero
                contador += 1
            else:
                posicion = 1

        print("Su promedio de la serie dada es: ",(total/(contador)))
        