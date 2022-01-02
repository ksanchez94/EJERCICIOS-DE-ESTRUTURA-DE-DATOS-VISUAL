def Ejercicio_6(self):
        #   Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.

        Lado_A=int(input("ingrese el la distancia (cm) de el LADO A: "))
        Lado_B=int(input("ingrese el la distancia (cm) de el LADO B: "))

        print("El lado A es de: ", Lado_A,"(cm)")
        print("El lado B es de: ", Lado_B,"(cm)")
        ladoA=Lado_A*Lado_A
        ladoB=Lado_B*Lado_B
        hipot= ladoA + ladoB
        hipotensa=hipot ** 0.5
        hipotensa1=round(hipotensa,2)
        print("LA Hipotenusa es de: ",hipotensa1,"(cm)")


