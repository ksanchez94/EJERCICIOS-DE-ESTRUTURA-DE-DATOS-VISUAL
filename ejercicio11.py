def Ejercicio_11(self):
        #   Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades, 
        #   decenas, centenas y unidades de mil.


        cantidad=int(input("ingrese cantidad (*4dijitos*): "))

        umil = cantidad / 1000
        tmp = cantidad % 1000

        cent = tmp / 100
        tmp = tmp % 100

        dece = tmp / 10
        unid = tmp % 10


        print ("Unidades de millar: %i" % umil )
        print ("Centenas: %i" % cent)
        print ("Decenas: %i" % dece)
        print ("Unidades: %i" % unid)