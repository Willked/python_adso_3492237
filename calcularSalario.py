# entradas
horasTrabajadas = input("Ingrese el numero de horas trabajadas: ")
valorHora = input("Ingrese el valor de la hora trabajada: ")

#proceso
salarioBruto = float(horasTrabajadas) * float(valorHora)
descuento = salarioBruto * 0.12
salarioNeto = salarioBruto - descuento

#salidas
print("El salario bruto es: ", salarioBruto)
print("El descuento es: ", descuento)
print("El salario neto es: ", salarioNeto)