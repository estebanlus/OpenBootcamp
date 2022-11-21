#Alumno y calificaciones

class Alumno:
    nombre = ""
    nota = 0
    
    def __init__(self, nombre = "NN", nota = 1):
        self.nombre = nombre
        self.nota = nota

    def muestraDatos(self):
        print("El alumno", self.nombre, "ha obtenido una nota de", self.nota)

    def muestraResultado(self):
        if self.nota >= 6:
            print("El alumno ha aprobado con una nota de", self.nota)
        else:
            print("El alumno ha desaprobado con una nota de", self.nota)

alumno = Alumno("Juan Perez", 8)
alumno.muestraDatos()
alumno.muestraResultado()

alumno2 = Alumno("Natalia Natalia", 4)
alumno2.muestraDatos()
alumno2.muestraResultado()
