

def main():
	r1 = 42
	r2 = 24
	

	if(euclides(r1,r2)):
		print(str(r1) + " y " + str(r2) + " son primos relativos")
	else:
		print(str(r1) + " y " + str(r2) + " no son primos relativos")


def euclides(r1, r2):
	if r2>r1 or r2<0:
		print("Condición 0 <= r2 <= r1 no cumplida")
		return False

	auxR1 = r1
	auxR2 = r2
	auxR4 = 1

	while auxR4 != 0:

		auxR3 = auxR1 // auxR2
		auxR4 = auxR1 % auxR2

		print(str(auxR1) + "  = " + str(auxR3) + " x " + str(auxR2) + " + " + str(auxR4))

		auxR1 = auxR2
		auxR2 = auxR4

		if auxR2 == 1:
			"""print(str(r1) + " y " + str(r2) + " son primos relativos")"""
			return True


	return False

main()