#!/usr/bin/env python
"""Queremos programar un generador de password que cumpla las siguientes condiciones:
a. Una password debe tener los atributos longitud y contraseña. Por defecto la longitud será 8.
b. Podremos generar una contraseña por defecto de longitud 8 o generar una contraseña aleatoria con una longitud dada.
c. Deberemos poder comprobar si es fuerte dicha contraseña. Para que una contraseña sea fuerte debe tener más de 2 mayúsculas, más de 1 minúscula y más de 5 números.
d. Deberemos poder generar una password, es decir, generar la contraseña del objeto según la longitud que tenga.
e. Debemos poder obtener la contraseña y la longitud de una password.
f. Debemos poder modificar la longitud de una passsword.
Para probarlo:
- Crea un array de password con el tamaño solicitado por teclado.
- Genera las contraseñas y muestra si son o no fuertes."""

import random

class Password():
    """CONSTRUCTORES"""
    def __init__(self,String pwd):
        self.pwd=str(pwd)
        self.longitud = len(pwd)

    def __init__(self):
        self.pwd=random.randint(0, 99999999)
        self.longitud = len(self.pwd)

    def __int__(self,longitud):
        self._pwd = random.randint(0, (10 ^ longitud) - 1)

    """GETTERS & SETTERS"""
    @property
    def pwd(self):
        self._pwd

    @property
    def longitud(self):
        self._longitud

    @pwd.setter
    def contraseña(self,pwd):
        if len(pwd)==8:
            self._pwd=pwd
        else:
            raise ValueError("Contraseña incorrecta, la longitud tiene que ser de 8 caracteres")


    def pwd(self,longitud):
        self._pwd= random.randint(0, (10^longitud)-1)

    @str
    def __str__(self):
        return self._pwd+" "

    def comprobar(self,pwd):
        print("DUDA")


if __name__ == "__main__":
    p1=Password()
