nombreCliente = input("Nombre del Cliente: ")
diasEstancia = int(input("Dias de estancia: "))
tarifaDiaria = 125900
tipoHabitacion = True
resultadoEstancia = diasEstancia * tarifaDiaria
print ("***Sistema de Reserva de Hoteles***")
print ("Cliente: ", nombreCliente)
print ("Dias de estancia: ", diasEstancia)
print ("Tarifa Diaria: ", tarifaDiaria)
print ("Habitación con vista al mar?", tipoHabitacion)
print ("Monto total: ", resultadoEstancia)