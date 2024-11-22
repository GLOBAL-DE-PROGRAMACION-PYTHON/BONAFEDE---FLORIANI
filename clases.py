#CLASE DETECTOR:

class Detector:

    def __init__(self, nombre="Detector ADN", tipo="ADN"):
        self.nombre = nombre
        self.tipo = tipo

#MÉTODOS PARA LA DETECCIÓN DE MUTACIONES:

    def detectar_mutantes(self, adn):
        if self._detectar_horizontal(adn) or self._detectar_vertical(adn) or self._detectar_diagonal(adn):
            return True
        return False

    def _detectar_horizontal(self, adn):
        for item in adn:
            if self._contiene_secuencia_mutante(item):
                return True
        return False

    def _detectar_vertical(self, adn):
        tamanio = len(adn)
        secuencia = ""
        for i in range(tamanio):
            for grupo in adn:
                secuencia = secuencia + grupo[i]
            if self._contiene_secuencia_mutante(secuencia):
                return True
            secuencia = ""
        return False

    def _contiene_secuencia_mutante(self, secuencia):
        tamanio = len(secuencia)
        for i in range(tamanio):
            if (i + 3 >= tamanio):
                return False
            if (secuencia[i] == secuencia[i + 1] == secuencia[i + 2] == secuencia[i + 3]):
                return True

    def _detectar_diagonal(self, adn):
        tamanio = len(adn)
        for i in range(tamanio):
            if (i + 3) >= tamanio:
                break
            tamanioColumn = len(adn[i])
            for j in range(tamanioColumn):
                if (j + 3) >= tamanioColumn:
                    break
                if self._verificar_diagonal(adn, i, j):
                    return True
        return False

    def _verificar_diagonal(self, adn, i, j):
        secuencia = ""
        secuenciaSecundaria = ""
        for k in range(4):
            secuencia = secuencia + adn[i + k][j + k]
            maxColumn = len(adn[i]) - 1
            secuenciaSecundaria = secuenciaSecundaria + adn[i + k][maxColumn - j - k]
        isMutantePrincipal = self._contiene_secuencia_mutante(secuencia)
        if isMutantePrincipal:
            return True
        isMutanteSecundaria = self._contiene_secuencia_mutante(secuenciaSecundaria)
        if isMutanteSecundaria:
            return True
        return False

#CLASE MUTADOR:

class Mutador:

    def __init__(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        self.base_nitrogenada = base_nitrogenada
        self.posicion_inicial = posicion_inicial
        self.orientacion_de_la_mutacion = orientacion_de_la_mutacion

    def crear_mutante(self):
        pass


#CLASE RADIACIÓN:

class Radiacion(Mutador):

    def __init__(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        super().__init__(base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion)


#MÉTODO PARA CREAR MUTANTES HORIZONTALES O VERTICALES:

    def crear_mutante(self, matriz):
        fila, columna = map(int, self.posicion_inicial.split(','))
        fila -= 1  # Ajustar la fila para que comience en 0
        columna -= 1  # Ajustar la columna para que comience en 0
        if self.orientacion_de_la_mutacion == 'H':
            for i in range(4):
                if columna + i >= len(matriz[0]):
                    raise ValueError("Posición fuera de rango para mutación horizontal.")
                matriz[fila] = matriz[fila][:columna + i] + self.base_nitrogenada + matriz[fila][columna + i + 1:]
        elif self.orientacion_de_la_mutacion == 'V':
            for i in range(4):
                if fila + i >= len(matriz):
                    raise ValueError("Posición fuera de rango para mutación vertical.")
                matriz[fila + i] = matriz[fila + i][:columna] + self.base_nitrogenada + matriz[fila + i][columna + 1:]
        return matriz


#CLASE VIRUS:


class Virus(Mutador):


    def __init__(self, base_nitrogenada):
        super().__init__(base_nitrogenada)

#MÉTODO PARA CREAR MUTACION DIAGONAL:

    def crear_mutante(self, base_nitrogenada, posicion_inicial, matriz):
        self.matriz = matriz
        fila, columna = map(int, posicion_inicial.split(','))
        fila -= 1  # Ajustar la fila para que comience en 0
        columna -= 1  # Ajustar la columna para que comience en 0
        for i in range(4):
            if fila + i >= len(matriz) or columna + i >= len(matriz[0]):
                raise ValueError("Posición fuera de rango para mutación diagonal.")
            matriz[fila + i] = matriz[fila + i][:columna + i] + base_nitrogenada + matriz[fila + i][columna + i + 1:]
        return matriz


#CLASE SANADOR:

import random

class Sanador:

    def __init__(self):
        self.detector = Detector()
        self.mutaciones_detectadas = 0
        self.mutaciones_sanadas = 0


#MÉTODOS PARA SANAR MUTANTES:

    def sanar_mutantes(self, matriz):
        if self.detector.detectar_mutantes(matriz):
            self.mutaciones_detectadas += 1
            return self._generar_adn_nuevo()
        return matriz

    def _generar_adn_nuevo(self):
        bases = ['A', 'T', 'C', 'G']
        nuevo_adn = []
        while True:
            fila = ''.join(random.choices(bases, k=6))
            nuevo_adn.append(fila)
            if len(nuevo_adn) == 6:
                    break
        if self.detector.detectar_mutantes(nuevo_adn):
          return self._generar_adn_nuevo()
        self.mutaciones_sanadas += 1
        return nuevo_adn