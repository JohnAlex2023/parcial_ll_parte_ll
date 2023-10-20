# main.py
from MODEL.productos import ControlPlagas, ControlFertilizantes, Antibiotico
from MODEL.facturas import Factura
from CRUD.CRUD_CLIENTES import GestorClientes

def mostrar_factura(cliente):
    factura = cliente.facturas[-1]  # Obtener la última factura generada
    print("\n\t--------------------------------------------------------")
    print("\t|                   FACTURA DE COMPRA                   |")
    print("\t--------------------------------------------------------")
    print(f"\tNombre del cliente: {cliente.nombre}")
    print(f"\tCédula del cliente: {cliente.cedula}")
    print(f"\tFecha de la factura: {factura.fecha}")
    print("\t--------------------------------------------------------")
    print("\t|    Producto    |    Precio Unitario    |    Cantidad    |    Total    |")
    print("\t--------------------------------------------------------")
    for producto in factura.productos:
        total_producto = producto.valor * producto.cantidad
        print(f"\t|{producto.nombre:<16}|{producto.valor:>23,.2f}|{producto.cantidad:>16}|{total_producto:>13,.2f}|")
    print("\t--------------------------------------------------------")
    print(f"\tTotal a pagar: {factura.calcular_total():,.2f}")
    print("\t--------------------------------------------------------")
    print("\n\tGracias por comprar aquí. Ha finalizado la compra.")

def main():
    print("\n\n\t ________________________________________________________")
    print("\t|                   TIENDA DEL CAMPO                     |")
    print("\t|  Productos agrícolas, Pesticidas, fertilizantes y más  |")
    print("\t|________________________________________________________|")
    gestor_clientes = GestorClientes()

    while True:
        print("\n\tSeleccione una operación:")
        print("\t1. Crear cliente")
        print("\t2. Buscar cliente")
        print("\t3. Actualizar información de cliente")
        print("\t4. Eliminar cliente")
        print("\t5. Realizar compra")
        print("\t6. Ver toda la información de un cliente")
        print("\t7. Salir")

        opcion = input("\tIngrese el número de opción: ")

        if opcion == "1":
            nombre = input("\n\tIngrese el nombre del cliente: ")
            cedula = input("\tIngrese la cédula del cliente: ")
            cliente = gestor_clientes.crear_cliente(nombre, cedula)
            print(f"\tCliente {cliente.nombre} creado con éxito.")
        elif opcion == "2":
            cedula = input("\tIngrese la cédula del cliente a buscar: ")
            cliente = gestor_clientes.buscar_cliente(cedula)
            if cliente:
                print(f"\tNombre del cliente: {cliente.nombre}")
                print(f"\tCédula del cliente: {cliente.cedula}")
            else:
                print("\tCliente no encontrado.")
        elif opcion == "3":
            cedula = input("\tIngrese la cédula del cliente a actualizar: ")
            nuevo_nombre = input("\tIngrese el nuevo nombre del cliente: ")
            nueva_cedula = input("\tIngrese la nueva cédula del cliente: ")
            if gestor_clientes.actualizar_cliente(cedula, nuevo_nombre, nueva_cedula):
                print("\tCliente actualizado con éxito.")
            else:
                print("\tCliente no encontrado.")
        elif opcion == "4":
            cedula = input("\tIngrese la cédula del cliente a eliminar: ")
            if gestor_clientes.eliminar_cliente(cedula):
                print("\tCliente eliminado con éxito.")
            else:
                print("\tCliente no encontrado.")
        elif opcion == "5":
            cedula = input("\tIngrese la cédula del cliente que realizará la compra: ")
            cliente = gestor_clientes.buscar_cliente(cedula)
            if cliente:
                productos_factura = []

                while True:
                    print("\n\tSeleccione un tipo de producto:")
                    print("\t1. Control de Plagas")
                    print("\t2. Control de Fertilizantes")
                    print("\t3. Antibiótico")
                    print("\t4. Finalizar compra")

                    opcion_compra = input("\tIngrese el número de opción: ")

                    if opcion_compra == "1":
                        ica = input("\n\tIngrese el registro ICA: ")
                        nombre = input("\tIngrese el nombre del producto: ")
                        frecuencia_aplicacion = input("\tIngrese la frecuencia de aplicación (En días): ")
                        valor = float(input("\tIngrese el valor del producto: "))
                        periodo_carencia = input("\tIngrese el periodo de carencia en días: ")
                        cantidad = int(input("\tIngrese la cantidad a comprar: "))
                        producto = ControlPlagas(ica, nombre, frecuencia_aplicacion, valor, periodo_carencia, cantidad)
                        productos_factura.append(producto)
                    elif opcion_compra == "2":
                        ica = input("\n\tIngrese el registro ICA: ")
                        nombre = input("\tIngrese el nombre del producto: ")
                        frecuencia_aplicacion = input("\tIngrese la frecuencia de aplicación (En días): ")
                        valor = float(input("\tIngrese el valor del producto: "))
                        ultima_aplicacion = input("\tIngrese la fecha de la última aplicación (DD-MM-AA): ")
                        cantidad = int(input("\tIngrese la cantidad a comprar: "))
                        producto = ControlFertilizantes(ica, nombre, frecuencia_aplicacion, valor, ultima_aplicacion, cantidad)
                        productos_factura.append(producto)
                    elif opcion_compra == "3":
                        tipo_animal = input("\n\tIngrese el tipo de animal (Bovinos, Caprinos o Porcinos): ")
                        nombre = input("\tIngrese el nombre del antibiótico: ")
                        dosis = input("\tIngrese la dosis (entre 400Kg y 600Kg): ")
                        valor = float(input("\tIngrese el valor del antibiótico: "))
                        cantidad = int(input("\tIngrese la cantidad a comprar: "))
                        producto = Antibiotico(nombre, dosis, tipo_animal, valor, cantidad)
                        productos_factura.append(producto)
                    elif opcion_compra == "4":
                        if productos_factura:
                            fecha_factura = input("\n\tIngrese la fecha de la factura (DD-MM-AAAA): ")
                            factura = Factura(fecha_factura, productos_factura)
                            cliente.facturas.append(factura)
                            mostrar_factura(cliente)
                            break
                        else:
                            print("\n\tNo se han seleccionado productos.")
                    else:
                        print("\n\tOpción no válida. Por favor, elija una opción válida.")

        elif opcion == "6":
            cedula = input("\tIngrese la cédula del cliente para mostrar facturas y productos vendidos: ")
            cliente = gestor_clientes.buscar_cliente(cedula)
            if cliente:
                gestor_clientes.buscar_por_cedula(cliente)
            else:
                print("\tCliente no encontrado.")

        elif opcion == "7":
            print("\n\tHa finalizado la sesión.")
            break
        else:
            print("\n\tOpción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()