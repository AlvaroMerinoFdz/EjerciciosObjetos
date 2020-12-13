class Telefono:
    "Clase teléfono"
    def __init__(self,numero):
        self.numero=numero

    def telefonear(self):
        print("Llamando")

    def colgar(self):
        print("Colgando")

    def __str__(self):
        return self.numero

class Camara:
    "Clase camara fotográfica"
    def __init__(self,mpx):
        self.mpx=mpx

    def fotografiar(self):
        print("Fotografiando")

    def __str__(self):
        return self.mpx

class Reproductor:
    "Clase reprodutcor mp3"
    def __init__(self,capacidad):
        self.capacidad=capacidad

    def reproducirmp3(self):
        print("Reproduciendo mp3")

    def reproducirvideo(self):
        print("Reproduciendo video")

    def __str__(self):
        return self.capacidad

class Movil(Telefono,Camara,Reproductor):

    def __init__(self,numero,mpx,capacidad):
        Telefono.__init__(self,numero)
        Camara.__init__(self,mpx)
        Reproductor.__init__(self,capacidad)

    def __str__(self):
        return "Número: {0}, Cámara: {1}, Capacidad: {2}".format(Telefono.__str__(self), Camara.__str__(self), Reproductor.__str__(self))

if __name__ == '__main__':
    mimovil = Movil("634714357","5Mpx","1Gb")
    print(dir(mimovil))
    print(mimovil)

