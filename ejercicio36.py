 def Ejercicio4_4(self):
        #En una empresa pagan según las horas trabajadas y una tarifa fija por hora. Si la 
        #cantidad de horas trabajadas en una semana es mayor a 40, la tarifa se 
        #incrementa en un 35% para las horas extras. Escribe una acción principal que 
        #solicite la identificación de 5 empleados, el monto cancelado por hora, y la 
        #cantidad de horas trabajadas por cada uno, llame a acciones/funciones que 
        #calculen el salario semanal por horas trabajadas (<=40) y los ingresos por 
        #concepto de horas extras, y finalmente informe los resultados en la acción 
        #principal.


        identificacion = {}
        acp = Ejercicios()

        while len(identificacion) <= 4:
            nombre = input("Ingrese su identificación(nombre): ")
            identificacion[nombre] = int(input("Ingrese horas trabajadas{}: ".format(nombre)))
        tarifa = int(input("Ingrese el monto por hora: "))

        salario = acp.CalSalSem(identificacion,tarifa)
        for i in salario:
            print(i,"cobrará",salario[i][1])

    def CalSalSem(self,identificacion,tarifa):
        Calculo_principal = Ejercicios()
        for i in identificacion:
            if identificacion[i] <= 40:
                identificacion[i] = [identificacion[i],(identificacion[i]*tarifa)]
            else:
                identificacion[i] = [identificacion[i],(40*tarifa)]
                identificacion[i][1] = Calculo_principal.CalIngHExt(identificacion[i],tarifa)
        print("*"*20)
        return identificacion

def CalIngHExt(self,identificacion,tarifa):
    extra = identificacion[1] + ((identificacion[0]-40) *(tarifa + (tarifa * 0.35)))
    return extra
