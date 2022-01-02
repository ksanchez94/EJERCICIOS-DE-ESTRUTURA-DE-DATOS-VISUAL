def Ejercicio2_7(self):
        #   El IMC resulta de la división de la masa del individuo (en kilogramos) entre el 
        #   cuadrado de la estatura (en metros). El índice de masa corporal es un indicador 
        #   del peso de una persona en relación con su altura.
        #   Clasificación del IMC de acuerdo con la OMS de la ONU:
        #   a. Menor a 16: Criterio de ingreso.
        #   b. 16 a 16.9: infra peso.
        #   c. 17 a 18.4: bajo peso.
        #   d. 18.5 a 24.9: peso normal.
        #   e. 25 a 29.9: sobrepeso.
        #   f. 30 a 34.9: obesidad pre-mórbida.
        #   g. 40 a 45: obesidad mórbida.
        #   h. Mayor a 45: obesidad híper-mórbida.
        #   Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en 
        #   centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor 
        #   de IMC de la persona y la categoría en la cual fue clasificado.

        libra=0
        while libra<=0:
            libra=int(input("ingrese su masa(libras): "))

        estatura=0
        while estatura<=0:
            estatura=float(input("ingrese su estatura (en metros): "))
        masa=libra/2.2046


        imc=masa/(estatura**2)

        imc1=round(imc,2)

        if imc<=16:
            print("*Criterio de ingreso.*")
        elif imc>16 and imc <= 18.4:
            print("*Bajo peso.*")
        elif imc>=17 and imc <=  18.4:
            print("*Bajo peso.*")
        elif imc>=18.5 and imc <= 24.9:
            print("*Peso normal.*")
        elif imc>=25 and imc <=29.9:
            print("*Sobrepeso.*")
        elif imc>=30 and imc <=39.9:
            print("*Obesidad pre-mórbida.*")
        elif imc>=40 and imc <=45:
            print("*Obesidad mórbida.*")
        elif imc >=45:
            print("*Obesidad híper-mórbida.*")

        print("El valor de IMC de la persona es:",imc1)
