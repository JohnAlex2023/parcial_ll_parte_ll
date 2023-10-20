from MODEL.clientes import Cliente

class GestorClientes:
    def __init__(self):
        self.lista_de_clientes = []

    def crear_cliente(self, nombre, cedula):
        cliente = Cliente(nombre, cedula)
        self.lista_de_clientes.append(cliente)
        return cliente

    def buscar_cliente(self, cedula):
        for cliente in self.lista_de_clientes:
            if cliente.cedula == cedula:
                return cliente
        return None
    
    def actualizar_cliente(self, cedula, nuevo_nombre, nueva_cedula):
        cliente = self.buscar_cliente(cedula)
        if cliente:
            cliente.nombre = nuevo_nombre
            cliente.cedula = nueva_cedula
            return True
        return False 
    
    def eliminar_cliente(self, cedula):
        cliente = self.buscar_cliente(cedula)
        if cliente:
            self.lista_de_clientes.remove(cliente)
            return True
        return False

   
    def buscar_por_cedula(self, cliente):
        print(f"\n\tNombre del cliente: {cliente.nombre}")
        print(f"\tCédula del cliente: {cliente.cedula}")

        if cliente.facturas:
            for factura in cliente.facturas:
                print("\n\t--------------------------------------------------------")
                print("\t|                   FACTURA DE COMPRA                   |")
                print("\t--------------------------------------------------------")
                print(f"\tFecha de la factura: {factura.fecha}")
                print("\t--------------------------------------------------------")
                print("\t|    Producto    |    Precio Unitario    |    Cantidad    |    Total    |")
                print("\t--------------------------------------------------------")
                total_factura = 0  # Variable para almacenar el total de la factura
                for producto in factura.productos:
                    total_producto = producto.valor * producto.cantidad
                    total_factura += total_producto  # Sumar al total de la factura
                    print(f"\t|{producto.nombre:<16}|{producto.valor:>23,.2f}|{producto.cantidad:>16}|{total_producto:>13,.2f}|")
                print("\t--------------------------------------------------------")
                print(f"\tTotal a pagar: {total_factura:,.2f}")  # Mostrar el total de la factura
                print("\t--------------------------------------------------------")

        else:
            print("\tEl cliente no tiene facturas.")
