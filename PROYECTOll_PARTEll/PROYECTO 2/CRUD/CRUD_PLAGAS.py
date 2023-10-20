from MODEL.productos import ControlPlagas

class GestorControlPlagas:
    def __init__(self):
        self.lista_de_control_plagas = []

    def crear_control_plagas(self, ica, nombre, frecuencia_aplicacion, valor, periodo_carencia, cantidad):
        producto = ControlPlagas(ica, nombre, frecuencia_aplicacion, valor, periodo_carencia, cantidad)
        self.lista_de_control_plagas.append(producto)
        return producto

    def buscar_control_plagas_por_nombre(self, nombre):
        for producto in self.lista_de_control_plagas:
            if producto.nombre == nombre:
                return producto
        return None

    def actualizar_control_plagas(self, nombre, nuevos_valores):
        producto = self.buscar_control_plagas_por_nombre(nombre)
        if producto:
            for clave, valor in nuevos_valores.items():
                setattr(producto, clave, valor)
            return producto
        return None

    def eliminar_control_plagas(self, nombre):
        producto = self.buscar_control_plagas_por_nombre(nombre)
        if producto:
            self.lista_de_control_plagas.remove(producto)
            return producto
        return None
