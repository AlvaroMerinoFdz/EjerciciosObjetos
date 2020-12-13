#!/usr/bin/env python
import random

class Password():
    def __init__(self,contraseña):
        self.contraseña=contraseña
        self.longitud = len(contraseña)

    def __init__(self):
        self.contraseña=random.randint(0, 99999999)
        self.longitud = len(contraseña)

    #GETTERS & SETTERS
    @property
    def contraseña(self):
        self._contraseña

    @property
    def longitud(self):
        self._longitud

    @contraseña.setter
    def contraseña(self,contraseña):
        if len(contraseña)==8:
            self._contraseña=contraseña
        else:
            raise ValueError("Contraseña incorrecta, la longitud tiene que ser de 8 caracteres")


    def contraseña(self,longitud):
        self._contraseña= random.randint(0, (10^longitud)-1)

    @str
    def __str__(self):
        return self._contraseña+" "

    def comprobar(self,contraseña):
        print("DUDA")


if __name__ == "__main__":
    p1=Password(12345678)
    #contraseña()
    #contraseña(12345)