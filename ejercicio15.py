def Ejercicio2_4(self):
        #   Para un valor entero positivo que representa una cantidad en segundos, indicar 
        #   su equivalente en minutos, horas y días.


        numero=0
        while numero<=0:
            numero=int(input("ingrese cantidad deseada: "))


        dia= numero/86400
        horas= numero/3600
        minutos= numero/60

        print("Días: ", dia )
        print("Horas: ",horas)
        print("Minutos: ", minutos)