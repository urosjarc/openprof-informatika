class Node:
	def __init__(self, vrednost: int):
		self.vrednost = vrednost
		self.otroci: list[Node] = []


n1 = Node(0)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(4)

n1.otroci = [n2, n3]
n2.otroci = [n4]
n4.otroci = [n5]


def izpisi():
	"""
	* Ustvari funkcijo ki sprejme objekt razreda `Node`.
	* Izpisi vrednost objekta ter vrednosti vseh elementov v drevesu.
	"""

	def funkcija(node: Node):
		print(node.vrednost)
		for otrok in node.otroci:
			funkcija(otrok)

	print(f"Vsota je: {funkcija(n1)}")


def vsota():
	"""
	* Ustvari funkcijo ki sprejme objekt razreda `Node`.
	* Vrni iz funkcije vsoto vseh vrednosti elementov v drevesu.
	"""

	def funkcija(node: Node, vsota: int = 0):
		vsota += node.vrednost
		for otrok in node.otroci:
			vsota += funkcija(otrok)
		return vsota

	print(f"Vsota je: {funkcija(n1)}")
