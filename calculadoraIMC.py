peso = int(input ("Ingrese su peso en kg: "))
altura = float(input ("Ingrese su altura en metros: "))

IMC = peso / altura ** 2

if IMC < 18.5:
    print ("IMC: ", round(IMC, 2), "Bajo peso")
elif 18.5 <= IMC < 24.9:
    print ("IMC: ",round(IMC, 2), "Peso normal")
elif 25 <= IMC < 29.9:
    print ("IMC: ",round(IMC, 2), "Sobrepeso")
else:
    print("IMC: ",round(IMC, 2), "Obesidad")