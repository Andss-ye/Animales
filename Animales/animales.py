class Animales:
    def __init__(self, edad, peso, raza):
        self.edad = edad
        self.peso = peso
        self.raza = raza
    def saludar(self):
        pass
    def mostrar_info(self):
        return(self.edad, self.peso, self.raza)

class Gato(Animales):
    def saludar(self):
        return "Miau"
class Perro(Animales):
    def saludar(self):
        return "Guau"
class Conejo(Animales):
    def saludar(self):
        return "zzz"
class Pez(Animales):
    def saludar(self):
        return "Glu, glu"
