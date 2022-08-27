class Marca:

    def __init__(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

class Control:

    def __init__(self):
        self.tv = None

    def enlazar(self, tv):
        self.tv = tv
        self.tv.setControl(self)

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()


    def volumenUp(self):
        self.tv.volumenUp()


    def volumenDown(self):
        self.tv.volumenDown()


    def setCanal(self, canal):
        self.tv.setCanal(canal)

    def setTV(self,tv):
        self.tv = tv
    
    def getTV(self):
        return self.tv


class TV:

    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.control = None

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control

    def setPrecio(self, precio):
        self.precio = precio
    
    def getPrecio(self):
        return self.precio

    def setVolumen(self, volumen):
        if (volumen >= 0 and volumen <= 7):
            self.volumen = volumen

    def getVolumen(self):
        return self.volumen

    def setCanal(self, canal):
        if (canal >= 1 and canal <= 120):
            self.canal = canal
    
    def getCanal(self):
        return self.canal

    def getEstado(self):
        return self.estado

    @classmethod
    def setnumTV(cls, numTV):
        cls.numTV = numTV

    @classmethod
    def getnumTV(cls):
        return cls.numTV

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if (self.estado and self.canal < 120):
            self.canal += 1

    def canalDown(self):
        if (self.estado and self.canal > 1):
            self.canal -= 1

    def volumenUp(self):
        if (self.estado and self.volumen < 7):
            self.volumen += 1

    def volumenDown(self):
        if (self.estado and self.volumen > 0):
            self.volumen -= 1


