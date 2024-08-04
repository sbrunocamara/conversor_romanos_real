# classes/numero.py
class Real:
    def __init__(self, numero):
        self.numero = numero
    
    def converteRealParaRomano(self):
        romano = self._converteParaRomano(self.numero)
        return romano
           
    def _converteParaRomano(self, numero):
        
        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        resultado = ""

        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor

        return resultado