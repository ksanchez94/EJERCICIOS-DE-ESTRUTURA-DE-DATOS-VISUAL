def Ejercicio2_10(self):
        #   En un almacén se hace un 20% de descuento a los clientes cuya compra supere 
        #   los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a 
        #   pagar por el cliente y arroje como salida el monto aplicando el descuento de ser 
        #   necesario.


        numero=0
        while numero<=0:
            numero=int(input("ingrese cantidad deseada: "))

        if numero>=1000:
            descuento=numero*0.2
            total=numero-descuento
            print("su monto a pagar es de:", total)
        else:
            print("su monto a pagar es de:",numero)
