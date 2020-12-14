#!/usr/bin/env python

import random
import string


class Password:
    """Generador de contraseñas aleatorias"""

    def generador(self, longitud):
        caracter = string.ascii_letters + string.digits
        return "".join(random.choice(caracter) for _ in range(longitud))

    """Comprobar la contraseña"""

    def comprobar(self, pwd):
        if sum(c.islower() for c in pwd) < 1 or sum(c.isupper() for c in pwd) < 2 or sum(c.isdigit() for c in pwd) < 5:
            return False
        else:
            return True

    """CONSTRUCTOR"""

    def __int__(self, longitud=8):
        self.pwd(longitud)
        self.longitud(self.pwd)

    """GETTERS & SETTERS"""

    @property
    def pwd(self):
        return self.pwd

    @property
    def longitud(self):
        return self.longitud

    @pwd.setter
    def pwd(self, longitud=8):
        if longitud <= 0:
            raise ValueError("La longitud no puede ser negativa")
        else:
            self.pwd = self.generador(longitud)

    @longitud.setter
    def longitud(self, pwd):
        len(pwd)

    """To string"""

    def __str__(self) -> str:
        clase = type(self).__name__
        mensaje = "{0}: {1}"
        return mensaje.format(clase, self.pwd)


if __name__ == "__main__":
    p1 = Password()
