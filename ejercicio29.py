def Ejercicio3_7(self):
        #   Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad, 
        #   peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con 
        #   base en dicha secuencia se desea realizar un estudio a fin de conocer:
        #   Edad promedio de todas las personas en la muestra.
        #   Peso promedio de todas las personas en la muestra.
        #   Estatura promedio de todas las personas en la muestra.
        #   Cuántas personas hay con edad entre los 18 y 25 años.
        #   Cuántas personas son mayores a 36 años.
        #   Cuál es el promedio de peso de las personas con edades entre 18 y 35 
        #   años.

        a = 0
        posicion = ["La edad", "El peso(kg)", "La estatura(cm)"]
        lista = [24, 74, 182, 30, 70, 170, 41, 60, 169, 22, 75, 183, 31, 83, 178, 35, 76, 172, 22, 68, 164, 23, 77, 163,
                23, 58, 163, 26, 89, 185, 23, 55, 162, 26, 47, 160, 26, 60, 163, 22, 54, 170, 23, 58, 165, 26, 75, 178,
                24, 65, 170, 28, 82, 177, 42, 85, 183, 25, 75, 174, 35, 53, 150, 19, 60, 169, 35, 59, 160, 45, 74, 162,
                40, 58, 160, 33, 69, 167, 55, 70, 158, 24, 64, 160, 29, 79, 180, 52, 69, 160, 42, 78, 169, 34, 63, 152, 0]

        personas = [0, 0, 0,0]
        acumulador = [0, 0, 0]
        contador = 0
        while a < 3: # 3 para control de posición de lista acumulador
                acumulador[a] = acumulador[a] + lista[contador]

                if lista[contador] == lista[96] or lista[contador] == lista[95] or lista[contador] == lista[94]:
                        a += 1
                        contador = 0
                        contador += a
                else:
                        if a == 0:
                                if lista[contador]>18 and lista[contador]<25:
                                        personas[0] += 1
                                        personas[3] += lista[contador+1]
                        elif lista[contador]>36:
                                personas[1] += 1
                        contador += 3

        for i in posicion:
                contador+=1
                print("{} promedio de todas las personas en la muestra es {}".format(i,round(((acumulador[contador-4])/32))))

        print("Hay {} personas con edad entre los 18 y 25 años con un peso promedio de {}".format(personas[0],round((personas[3]/personas[0]))))
        print("Hay {} personas mayores a 36 años".format(personas[1]))