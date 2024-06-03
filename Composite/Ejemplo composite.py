class Componente:
    def obtener_precio_total(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class Producto(Componente):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio_total(self):
        return self.precio

class Composite(Componente):
    def __init__(self):
        self.componentes = []

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def obtener_precio_total(self):
        precio_total = 0
        for componente in self.componentes:
            precio_total += componente.obtener_precio_total()
        return precio_total

# Definimos los componentes
gabinete = Producto("Gabinete", 50)
mouse = Producto("Mouse", 10)
teclado = Producto("Teclado", 15)
disco_duro = Producto("Disco Duro", 70)
tarjeta_madre = Producto("Tarjeta Madre", 100)
ram = Producto("RAM", 80)
cpu = Producto("CPU", 200)

# Creamos la estructura de la computadora utilizando Composite
perifericos = Composite()
perifericos.agregar_componente(mouse)
perifericos.agregar_componente(teclado)

gabinete_componentes = Composite()
gabinete_componentes.agregar_componente(disco_duro)
gabinete_componentes.agregar_componente(tarjeta_madre)

tarjeta_madre_componentes = Composite()
tarjeta_madre_componentes.agregar_componente(ram)
tarjeta_madre_componentes.agregar_componente(cpu)

gabinete_componentes.agregar_componente(tarjeta_madre_componentes)

mi_computadora = Composite()
mi_computadora.agregar_componente(gabinete)
mi_computadora.agregar_componente(perifericos)
mi_computadora.agregar_componente(gabinete_componentes)

print("Precio total de la computadora:", mi_computadora.obtener_precio_total())
print("Precio total del cpu:", cpu.obtener_precio_total())

