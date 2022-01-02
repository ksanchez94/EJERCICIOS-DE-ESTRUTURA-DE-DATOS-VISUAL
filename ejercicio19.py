 def Ejercicio2_8(self):
        #   Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año 
        #   2014 e imprima por pantalla el número de días que han pasado desde el 1 de 
        #   Enero de 2014 hasta la fecha dada.


        dia=int(input("ingrese una fecha (día): "))
        mes=int(input("ingrese una fecha (mes): "))

        lista=[31,59,90,120,151,181,212,243,273,304,334,365]


        if mes==1:
            lapso_de_tiempo=lista[0]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==2:
            lapso_de_tiempo=lista[1]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==3:
            lapso_de_tiempo=lista[2]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==4:
            lapso_de_tiempo=lista[3]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==5:
            lapso_de_tiempo=lista[4]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==6:
            lapso_de_tiempo=lista[5]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==7:
            lapso_de_tiempo=lista[6]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==8:
            lapso_de_tiempo=lista[7]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==9:
            lapso_de_tiempo=lista[8]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==10:
            lapso_de_tiempo=lista[9]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==11:
            lapso_de_tiempo=lista[10]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)
        elif mes==12:
            lapso_de_tiempo=lista[11]+dia
            print(" Dias que han pasado desde el 1 de Enero: ",lapso_de_tiempo)