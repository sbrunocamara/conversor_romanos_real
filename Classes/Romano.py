# classes/numero.py
class Romano:
    def __init__(self, romano):
        self.romano = romano

    def converteRomanoParaReal(self):
        real = self._converteParaReal(self.romano)
        return real    
    
    def _converteParaReal(self, romano):
        valores = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }

        numero = 0
        i = 0

        while i < len(romano):
            if i + 1 < len(romano) and romano[i:i+2] in valores:
                numero += valores[romano[i:i+2]]
                i += 2
            else:
                numero += valores[romano[i]]
                i += 1
                
        return numero