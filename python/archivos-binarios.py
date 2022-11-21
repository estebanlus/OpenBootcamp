class Vehiculo:
    marca = ""
    modelo = ""

    def __init__(self, marca = "Ford", modelo = "Focus"):
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f'El vehiculo es de marca {self.marca} y modeo {self.modelo}'

auto = Vehiculo("Hyundai", "Veloster")

fb = open('vehiculo.dat', 'wb')
pickle.dump(auto, fb)
fb.close()

f2 = open('vehiculo.dat', 'rb')
auto2 = pickle.load(f2)
f2.close()

print(auto2)
