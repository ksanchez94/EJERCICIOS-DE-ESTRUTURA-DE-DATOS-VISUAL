def Ejercicio2_6(self):
        #   En un estacionamiento el monto a pagar se calcula multiplicando el número de 
        #   horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se 
        #   incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
        #   Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada 
        #   y la hora de salida de un vehículo (las mismas corresponden a un mismo día) 
        #   calcule el monto a pagar por el dueño del vehículo.
        #   La entrada vendrá dada por dos enteros positivos el primero representa las horas 
        #   y el segundo los minutos, además por último se debe leer un carácter (A o P) que 
        #   indica si la hora es AM o PM.

        horas=0
        minutos=0
        salida=0

        while horas<=0 or horas>=13:
            horas=int(input("ingrese la hora de entrada horas : "))


        while minutos<=0 or minutos>=60:
            minutos=int(input("ingrese la hora de entrada minutos : "))

        am_pm=input("ingrese A o P: ")

        if am_pm=="a":
            am_pm_hora=horas+0
        else:
            am_pm_hora=horas+12

        while salida<=0 or salida>=12:
            salida=int(input("ingrese la hora de salida: "))




        am_pm=input("ingrese A o P: ")

        if am_pm=="a":
            am_pm_salida=salida+0
        else:
            am_pm_salida=salida+12



        if minutos>=30:
            valor_minutos=1*2.50
        else:
            valor_minutos=0+0

        minutos1=minutos*0.01
        lapso_de_tiempo=am_pm_salida-am_pm_hora
        lapso_de_tiempo1=lapso_de_tiempo+minutos1
        valor_hora=lapso_de_tiempo*4
        valor_total=(lapso_de_tiempo*4)+valor_minutos
        lapso_de_tiempo2=round(lapso_de_tiempo1,2)


        print("entrada: ",am_pm_hora)
        print("salida: ",am_pm_salida)
        print("minutos:",minutos)
        print("tiempo que estuvo estacionado : ",lapso_de_tiempo2)
        print("valor por cada media hora adicional: ",valor_minutos)
        print("valor por las hora:",valor_hora)
        print("valor total a pagar: ",valor_total)
