class Nave():
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("La clase se ha creado con exito!")

    def calificacion(self):
        codigo_legion = self.rango[0:1]
        identificador_coherte = self.rango[3]
        identificador_siglo = self.rango[4]
        identificador_escuadra = self.rango[5]
        numero_trooper = self.rango[6]

    def __str__(self):
        return f"La nave {self.nombre} tiene los siguientes atributos\nEl codigo de la legion es: {codigo_legion}; El identificador coherte: {identificador_coherte}; El identificador siglo: {identificador_siglo}; El identificador escuadra: {identificador_escuadra}; Numero trooper: {numero_trooper}"