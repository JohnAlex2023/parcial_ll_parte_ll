# En un archivo llamado crud_antibiotico.py

from MODEL.productos import Antibiotico

class GestorAntibioticos:
    def __init__(self):
        self.lista_de_antibioticos = []

    def crear_antibiotico(self, nombre, dosis, tipo_animal, valor, cantidad):
        producto = Antibiotico(nombre, dosis, tipo_animal, valor, cantidad)
        self.lista_de_antibioticos.append(producto)
        return producto

    def buscar_antibiotico_por_nombre(self, nombre):
        for producto in self.lista_de_antibioticos:
            if producto.nombre == nombre:
                return producto
        return None

    def actualizar_antibiotico(self, nombre, nuevos_valores):
        producto = self.buscar_antibiotico_por_nombre(nombre)
        if producto:
            for clave, valor in nuevos_valores.items():
                setattr(producto, clave, valor)
            return producto
        return None

    def eliminar_antibiotico(self, nombre):
        producto = self.buscar_antibiotico_por_nombre(nombre)
        if producto:
            self.lista_de_antibioticos.remove(producto)
            return producto
        return None
