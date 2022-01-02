def Ejercicio_9(self):
        #   Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. El bit 
        #   de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.

        numero=input("ingrese cantidad (*4dijitos*): ")
        contador=0


        numero_bit=str(numero)
        contador= int(numero_bit[0])+int(numero_bit[1])+int(numero_bit[2])+int(numero_bit[3])

        if contador  % 2==0:
            print("0")
        else: 
            print("1")