#Clase paquete

class Paquete:

    def __init__(self, x: int, y: int, piso: int, cinta_actual: int):
        self.x = x
        self.y = y
        self.piso = piso
        self.cinta_actual = cinta_actual
        self.velocidad = 1  # píxeles por frame
        self._sprite_vacio = (0, 0, 16, 8, 8, 15)  # Sprite caja vacía
        self._sprite_lleno = (0, 8, 16, 8, 8, 15)  # Sprite caja llena

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        if not isinstance(x, int):
            raise TypeError("La x debe ser un entero " + str(type(x)))
        elif x < 0:
            raise ValueError("La x no debe ser un número negativo")
        else:
            self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        if not isinstance(y, int):
            raise TypeError("La y debe ser un entero " + str(type(y)))
        elif y < 0:
            raise ValueError("La y no debe ser un número negativo")
        else:
            self.__y = y

    @property
    def piso(self) -> int:
        return self.__piso

    @piso.setter
    def piso(self, piso: int):
        if not isinstance(piso, int):
            raise TypeError("El piso debe ser un entero " + str(type(piso)))
        elif piso < 0:
            raise ValueError("El piso no debe ser un número negativo")
        else:
            self.__piso = piso

    @property
    def cinta_actual(self) -> int:
        return self.__cinta_actual

    @cinta_actual.setter
    def cinta_actual(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("La cinta debe ser un entero")
        elif valor < 0:
            raise ValueError("La cinta no puede ser negativa")
        else:
            self.__cinta_actual = valor

    def get_sprite(self):
        """Devuelve el sprite según si está en cinta 0 (vacío) o no (lleno)"""
        if self.cinta_actual == 0:
            return self._sprite_vacio
        else:
            return self._sprite_lleno

    def mover(self):
        """Mueve el paquete hacia la derecha según su velocidad"""
        self.x += self.velocidad

    def esta_en_extremo(self, limite_x: int) -> bool:
        """Verifica si el paquete llegó al extremo de la cinta"""
        return self.x >= limite_x

    def __str__(self) -> str:
        return f"Paquete en posición ({self.x}, {self.y}) en el piso {self.piso}, cinta {self.cinta_actual}"