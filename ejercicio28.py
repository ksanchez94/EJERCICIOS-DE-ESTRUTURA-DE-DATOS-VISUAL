 def Ejercicio3_6(self):
        #   Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que 
        #   informe al usuario qué valor tiene el número mayor y qué valor tiene el número 
        #   menor, sin contar el cero (0).

        lista=[]

        numero=int(input("ingrese cantidad deseada: "))
        while numero !=0:
            lista.append(numero)
            numero=int(input("ingrese cantidad deseada: "))


        mayor=max(lista) 
        print("numero mayor: ", mayor)
        menor=min(lista)
        print("numero menor: ", menor)