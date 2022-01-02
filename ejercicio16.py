def Ejercicio2_5(self):
        #   Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el 
        #   mayor? y ¿cuál es el segundo mayor?


        a=0
        b=0
        c=0
        while a<=0:
            a=int(input("Ingrese el primer numero entero positivo: "))
        while b<=0:   
            b=int(input("Ingrese el segundo numero entero positivo: "))
        while c<=0:
            c=int(input("Ingrese el tercer numero entero positivo: "))



        if a>b:   
            if a>c:
                print("Mumero mayor: ", a)
            else:
                print("Mumero mayor: ",c)
        else:
            if b>c:
                print("Mumero mayor: ",b)
            else:
                print("Mumero mayor: ",c)


        if a>b and a<c: 
            print("Mumero segundo mayor: ", a)
        if a<b and a>c: 
            print("Mumero segundo mayor: ", a)
        elif b>a and b<c:
            print("Mumero segundo mayor: ", b)
        elif b<a and b>c:
            print("Mumero segundo mayor: ", b)
        elif c>a and c<b:
            print("Mumero segundo mayor: ", c)
        elif c<a and c>b:
            print("Mumero segundo mayor: ", c)