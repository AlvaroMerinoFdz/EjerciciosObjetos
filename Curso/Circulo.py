class Circulo():
    def __init__(self,radio):
        self.set_radio(radio)
    @property
    def radio(self):
        print("Estoy dando el radio")
        return self._radio

    @radio.setter
    def set_radio(self,radio):
        if radio>=0:
            self._radio = radio
        else:
            self._radio = 0
            raise ValueError("El radio tiene que ser positivo")



    def get_radio(self):
        print("Estoy dando el radio")
        return self._radio

    @radio.deleter
    def radio(self):
        del self._radio

