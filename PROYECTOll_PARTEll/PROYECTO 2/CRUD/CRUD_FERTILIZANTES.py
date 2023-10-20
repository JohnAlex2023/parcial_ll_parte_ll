from MODEL.productos import ControlFertilizantes

class GestorControlFertilizantes:
    def __init__(self):
        self.lista_de_control_fertilizantes = []

    def crear_control_fertilizantes(self, ica, nombre, frecuencia_aplicacion, valor, ultima_aplicacion, cantidad):
        producto = ControlFertilizantes(ica, nombre, frecuencia_aplicacion, valor, ultima_aplicacion, cantidad)
        self.lista_de_control_fertilizantes.append(producto)
        return producto

    def buscar_control_fertilizantes_por_nombre(self, nombre):
        for producto in self.lista_de_control_fertilizantes:
            if producto.nombre == nombre:
                return producto
        return None

    def actualizar_control_fertilizantes(self, nombre, nuevos_valores):
        producto = self.buscar_control_fertilizantes_por_nombre(nombre)
        if producto:
            for clave, valor in nuevos_valores.items():
                setattr(producto, clave, valor)
            return producto
        return None

    def eliminar_control_fertilizantes(self, nombre):
        producto = self.buscar_control_fertilizantes_por_nombre(nombre)
        if producto:
            self.lista_de_control_fertilizantes.remove(producto)
            return producto
        return None
