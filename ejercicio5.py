def Ejercicio_5(self):
        #Dados tres (3) números, Hacer una aplicación que calcule la resolvente.

        a=0
        b=0
        c=0
        while a<=0:
            a=float(input("Ingrese el primer numero: "))
        while b<=0:   
            b=float(input("Ingrese el segundo numero: "))
        while c<=0:
            c=float(input("Ingrese el tercer numero: "))
        try:
            if a!=0:
                x1=(-b+((b**2)-(4*a*c)))/(2*a)
                x2=(-b-((b**2)-(4*a*c)))/(2*a)
                if x1==0 and x2==0:
                    print("solucion: x=%4.3f"%x1)
                else:
                    print("soluciones: x1=%4.3f y x2=%4.3f"%(x1,x2))
            else:
                if b!=0:
                    x=-c/b
                    print("solucion: x=%4.3f"%x)
                else:
                    if c!=0:
                        print("la ecuacion no tiene solucion.")
                    else:
                        print("la ecuacion tiene infinitas soluciones.")
        except:
            print("sin soluciones: no se pudo realizar la ecuacion con los datos introduciones.")