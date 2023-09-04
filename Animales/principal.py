from tienda import *
from animales import *

t = Tienda()

t.agregar_animales(Perro(5, 10, "Boxer"))
t.agregar_animales(Gato(2, 5, "Mestizo"))
t.agregar_animales(Conejo(0.5, 1, "....."))
t.agregar_animales(Pez(0.1, 0.050, "Golden"))

for i in range(4):
    a = t.entregar_animal()
    print(a.saludar(), a.mostrar_info())