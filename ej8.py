class Node:
  def __init__(self, nombre):
    self.nombre = nombre
    self.vecino = {}
    
  def add_neighbor(self, nodo, peso):
    self.vecino[nodo] = peso

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []
        self.padre = [i for i in range(vertices)]
        self.rango = [0 for i in range(vertices)]
        self.nombre_a_vertice = {}
        self.vertice_a_nombre = {}


    def agregar_arista(self, u, v, w):
        if u not in self.nombre_a_vertice:
            