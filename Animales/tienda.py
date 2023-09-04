from animales import *
from random import *

class Tienda:
    def __init__(self):
        self.animales = []
    def agregar_animales(self, animal):
        self.animales.append(animal)
    def entregar_animal(self):
        return choice(self.animales)