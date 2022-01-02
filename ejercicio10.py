 def Ejercicio_10(self):
        #   Dado un (1) número binario de cuatro (4) dígitos imprimir su valor

        cantidad=int(input("ingrese cantidad (*4dijitos*): "))

        umil = cantidad / 1000
        tmp = cantidad % 1000

        cent = tmp / 100
        tmp = tmp % 100

        dece = tmp / 10
        unid = tmp % 10

        unimil=round(umil)
        centena=round(cent)
        decenas=round(dece)
        unidad=round(unid)

        a_unimil= unimil*8
        a_centena= centena*4
        a_decenas= decenas*2
        a_unidad= unidad*1

        suma= a_unimil + a_centena + a_decenas + a_unidad

        print(suma)