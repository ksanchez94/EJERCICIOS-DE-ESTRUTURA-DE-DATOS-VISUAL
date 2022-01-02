def Ejercicio3_5(self):
        #   Dado un número entero N que representa una contraseña y asumiendo que una 
        #   contraseña debe tener al menos 10 dígitos para ser segura, determine si la 
        #   contraseña ingresada por el usuario es correcta, de no serlo debe pedirla 
        #   nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta 
        #   mostrar un mensaje de éxito al usuario, por salida estándar.
        contraseña=0
        while contraseña<=1000000000 or contraseña>=10000000000:
            contraseña=int(input("ingrese contraseña : "))


        if contraseña>=1000000000:
            print("**Contraseña correcta.**")
        else:
            print("**Contraseña incorrecta.**")