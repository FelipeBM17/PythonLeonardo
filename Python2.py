class Alumno:

    def inicializar(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=int(input("Ingrese su nota: "))

    def mostrar(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrarme_elestado(self):
        if self.nota>=3:
            print("APROBO")
        else:
            print("REPROBO")


# bloque principal

Alumno1=Alumno()
Alumno1.inicializar()
Alumno1.mostrar()
Alumno1.mostrarme_elestado()
