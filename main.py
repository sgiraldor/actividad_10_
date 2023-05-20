from abc import ABC, abstractmethod
import re


class ReglaValidacion(ABC):
    _longitud_esperada: int

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if self.longitud_esperada == 6:
            return len(clave) > self.longitud_esperada
        elif self.longitud_esperada == 8:
            return len(clave) > 8

    def _contiene_mayuscula(self, clave: str) -> bool:
        for letra in clave:
            if letra.isupper():
                return True
            else:
                return False

    def contiene_minuscula(self, clave: str) -> bool:
        for letra in clave:
            if letra.isupper():
                return False
            else:
                return True

    def contiene_numero(self, clave: str) -> bool:
        for letra in clave:
            if letra.isdigit():
                return True
            else:
                return False

    @abstractmethod
    def es_valida(self, clave) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)
        self.longitud_esperada = 8

    @staticmethod
    def contiene_caracter_especial(clave: str) -> bool:
        if not re.match("^[a-zA-Z]+$", clave):
            return True
        else:
            return False
    def es_valida(self, clave) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave):
        contador_mayusculas = 0
        clave_mayuscula = clave.upper()
        if clave.find(clave_mayuscula):
            for letra in clave:
                if letra.isupper():
                    contador_mayusculas += 1
                if contador_mayusculas >= 2 and contador_mayusculas != len(clave):
                    return True
            return False

    #def es_valida(self, clave) -> bool:
     #   if self._validar_longitud(clave):
      #      print("q")
       # if self.contiene_numero(clave):
        #    print("www")
        #if self.contiene_calisto(clave):
         #           return True


b = ReglaValidacionCalisto()
print(b.es_valida("CAlisto123"))
