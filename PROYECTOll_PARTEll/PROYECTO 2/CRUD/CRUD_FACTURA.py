from MODEL.facturas import Factura

class GestorFacturas:
    def __init__(self):
        self.lista_de_facturas = []

    def crear_factura(self, fecha, productos):
        factura = Factura(fecha, productos)
        self.lista_de_facturas.append(factura)
        return factura

    def buscar_factura_por_fecha(self, fecha):
        for factura in self.lista_de_facturas:
            if factura.fecha == fecha:
                return factura
        return None

    def actualizar_factura(self, fecha, nuevos_productos):
        factura = self.buscar_factura_por_fecha(fecha)
        if factura:
            factura.productos = nuevos_productos
            return factura
        return None

    def eliminar_factura(self, fecha):
        factura = self.buscar_factura_por_fecha(fecha)
        if factura:
            self.lista_de_facturas.remove(factura)
            return factura
        return None
