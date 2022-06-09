class Alumno:

    def inicializar(self):
        self.nombre=input("Ingrese el nombre")
        self.nota=int(input("Ingrese su nota"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=3:
            print("APROBO")
        else:
            print("MEDIOCRE")


# bloque principal

alumno1=Alumno()
alumno1.inicializar()
alumno1.imprimir()
alumno1.mostrar_estado()
