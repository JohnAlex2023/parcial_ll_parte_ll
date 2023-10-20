from MODEL.productos import ProductoControl

class GestorProductos:
    def __init__(self):
        self.lista_de_productos = []

    def crear_producto(self, ica, nombre, frecuencia_aplicacion, valor, cantidad, producto_tipo):
        producto = producto_tipo(ica, nombre, frecuencia_aplicacion, valor, cantidad)
        self.lista_de_productos.append(producto)
        return producto

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.lista_de_productos:
            if producto.nombre == nombre:
                return producto
        return None

    def actualizar_producto(self, nombre, nuevos_valores):
        producto = self.buscar_producto_por_nombre(nombre)
        if producto:
            for clave, valor in nuevos_valores.items():
                setattr(producto, clave, valor)
            return producto
        return None

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto_por_nombre(nombre)
        if producto:
            self.lista_de_productos.remove(producto)
            return producto
        return None
