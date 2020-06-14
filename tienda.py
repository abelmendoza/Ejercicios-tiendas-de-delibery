class Tienda:
    def __init__(self):
        self.nombre = []
        self.descripcion = []
        self.direccion = []
        self.categoria = []
        self.estado = []
    def menu(self):
        opciones = """
            1.- AGREGAR TIENDA
            2.- MOSTRAR TODAS LAS TIENDAS
            3.- BUSCAR TIENDAS POR CATEGORIA
            4.- VER TIENDA
        """
        print(opciones)
        eleccion = int(input("Elija una opcion:  \n"))
        if (eleccion == 1):
            print(self.agregarTienda())
            self.menu()
        elif (eleccion == 2):
            (self.mostrar())
            self.menu()
        elif (eleccion == 3):
            print(self.usuarioBuscar())
            self.menu()
        elif (eleccion == 4):
            print(self.usuarioBuscar())
            self.menu()
        elif (eleccion == 5):
            print("Transacciones realizadas")
        else:
            print("Elija una opcion del menu")
            self.menu()

    def agregarTienda(self):
        nombre = input("digite el nombre de la tienda: \n")
        descripcion = input("digite la descripcion: \n")
        direccion = input("digite la direccion: \n")
        categoria = input("digite la categoria: \n")

        print(self.guardarTienda(nombre, descripcion, direccion, categoria))
        agregarOtro = input("Desea registrar mas tiendas: y/n \n")
        if (agregarOtro == 's' or agregarOtro == 'S'):
                self.agregarTienda()
        return "Tiendas agregadas exitosamente"

    def guardarTienda(self, nombre, descripcion, direccion, categoria):
        self.nombre.append(nombre)
        self.descripcion.append(descripcion)
        self.direccion.append(direccion)
        self.categoria.append(categoria)
        self.estado=1
        return "Tienda {} registrada exitosamente..!!".format(nombre)

    def mostrar(self):
        for i in range(len(self.categoria)):

            self.detalle(i)
        pass
    def detalle(self, posicion):
        print("******TIENDA {} ****** ".format(self.nombre[posicion]))
        print("Productos {} ****** ".format(self.descripcion[posicion]))
        print("Direccion {} ****** ".format(self.direccion[posicion]))
        print("Categoria {} ****** ".format(self.categoria[posicion]))
        pass
    def usuarioBuscar(self):
        categoria= input("Escriba la categoria a buscar: \n")
        return self.buscarCategoria(categoria)
    def buscarCategoria(self, categoria):
        encontrado = False
        for i in range(len(self.nombre)):
            if (self.categoria[i] == categoria):
                encontrado = True
                self.detalle(i)
        if encontrado == False:
            print("No se escontraron resultados con la categoria {} ".format(categoria))
        pass
    def verTienda(self):
        posicion = int(input("Digite la posicion \n"))
        self.detalle(posicion)
        pass

tiendas = Tienda()
tiendas.guardarTienda("Pollos Kiky","Cuarto de pollo 15bs", "Doble via LG,5to anillo", "Restaurant")
tiendas.guardarTienda("Centro informatico", "Tv box Xiaomi 500bs", "Comercial Neval # 42", "Electronica")
tiendas.guardarTienda("El tren rojo", "Hamburguesas 12 bs" , "2do anillo", "Restaurant")
tiendas.guardarTienda("Ferreteria San Jorge", "Fierro de 2 pulgadas", "Doble via LG,6to anillo", "Ferreteria")
tiendas.menu()




