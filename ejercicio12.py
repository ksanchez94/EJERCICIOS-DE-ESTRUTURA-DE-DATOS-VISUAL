def Ejercicio2_1(self):
        #   exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos. 
        #   Usando estas premisas crea un algoritmo que lea una fecha como un número 
        #   entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si 
        #   el mismo es un año bisiesto o no.


        a = int(input("Ingrese fecha (ddmmaaaa): "))
        b = str(a)
        c = int(b[4] + b[5] + b[6] + b[7])
        lb = [(c%400),(c%4),(c%100)]

        res = False
        if lb[1] == 0 and not(lb[2] == 0):
            res = True

        if lb[0] == 0 or res:
            print("Es un año bisiesto")
        else:
            print("No es un año bisiesto")