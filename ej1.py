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
        return f"La nave {self.nombre} tiene los siguientes atributos\nEl codigo de la legion es: {codigo_legion}; El identificador coherte: {identificador_coherte}; El identificador siglo: {identificador_siglo}; El identificador escuadra: {identificador_escuadra}; Numero trooper: {numero_trooper}"


if __name__=="__main__":
    naves = [Nave("Ruben","AK-2890"),Nave("Nave Galactica","DK-0924"),Nave("Nave5","OK-1999")]
    for nave in naves:
        print(f"Nueva nave calificada: {nave.nombre}")
        print(nave.calificacion())