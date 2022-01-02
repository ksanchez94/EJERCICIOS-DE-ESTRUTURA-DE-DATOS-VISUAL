 def Ejercicio2_3(self):
        #   Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como 
        #   resultado su equivalente en segundos.


        horas=0
        minutos=0
        while horas<=0:
            horas=int(input("ingrese las horas: "))
        while minutos<=0:
            minutos=int(input("ingrese los minutos: "))

        segund= horas*3600
        segun= minutos*60

        segundos= segund+segun

        print("los segundos totales son: ", segundos )