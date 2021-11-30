numSecreto = [7,9,4,2]
intento = []
res = []

def adivinaNS():
	print("Bienvenido a este programa que consiste en adivinar el número secreto")
	print("Indicaciones:")
	print("1. El número secreto se conforma por 4 dígitos, ninguno se repite")
	print('2. Si uno de los dígitos forma parte del número secreto y no está en la posición correcta obtienes un "-"')
	print('3. Si uno de los dígitos forma parte del número secreto y está en la posición correcta obtienes un "*"')
	print("4. No hay límite en la cantidad de intentos por lo que el programa termina en cuanto adivines el número secreto")
	print("¡Suerte!, y recuerda que no te diré que dígito de los que has ingresado es el correcto, solo te daré pistas")
	print("para que logres descubrirlo")
	print("Ingresa el numero secreto:")

	salir = True
	numInt = 1
	while salir:
		res = []
		intento = list(map(int, input('Intento '+ str(numInt) +' > ')))
		
		for i in range(len(numSecreto)): 
			if intento[i] == numSecreto[i]:
				res.append("*")

		for i in range(4): 
			for j in range(4):
				if intento[i] != numSecreto[i]:
					if intento[i] == numSecreto[j]:
						res.append("-")
						break

		for i in range(4): 
			if intento[i] == numSecreto[i]:
				salir = False
			else:
				salir = True
				
				resulStr = ""
				for i in res:
					resulStr += str(i)
				print(resulStr)
				break
		numInt+=1
	print("Felicidades, adivinaste el número secreto")
adivinaNS()