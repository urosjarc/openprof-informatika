def pozitivnost():
	"""
	* Uporabnik vnese stevilko.
	* Izpisi ali je stevilka pozitivna!
	"""
	x = int(input("Vnesi stevilko: "))
	if x > 0:
		print("Je soda")
	else:
		print("Je liha")

def sodost():
	"""
	* Uporabnik vnese poljubno celo stevilko.
	* Izpisi ali je stevilka soda!
	"""
	x = int(input("Vnesi stevilko: "))
	if x % 2 == 0:
		print("Je soda")

def lihost():
	"""
	* Uporabnik vnese poljubno celo stevilko.
	* Izpisi ali je stevilka liha!
	"""
	x = int(input("Vnesi stevilko: "))
	if x % 2 == 1:
		print("Je liha")

def delitelji():
	"""
	* Uporabnik vnese poljubno celo stevilko.
	* Izpisi vse delitelje stevila!
	"""
	x = int(input("Vnesi stevilko: "))
	for i in range(x):
		if x % i == 0:
			print(i)

def prastevila():
	"""
	* Uporabnik vnese poljubno celo stevilko.
	* Preveri ali je stevilo prastevilo!
	"""
	x = int(input("Vnesi stevilko: "))
	prastevilo = True
	for i in range(x):
		if x % i == 0:
			prastevilo = False
	if prastevilo:
		print("Je prastevilo")
	else:
		print("Ni prastevilo")
