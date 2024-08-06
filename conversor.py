from Classes.Real import Real
from Classes.Romano import Romano
import re

print("Conversor de números!")
print('\n')

print(
    "1 - Converter número real para romano."
    +'\n'+
    "2 - Converter número romano para real."
    +'\n'+
     "3 - Sair."
    )

print('\n')
inputOption = input("Selecione a opção desejada: ")

def verificaNumeroReal(numero):
    try:
        # Tenta converter a string para um número inteiro
        int(numero)
        return True
    except (ValueError, TypeError):
        print('\n')
        print("O valor inserido deve ser um número inteiro válido!")
        print('\n')
        exit()

def verificaNumeroRomano(numero):
    # Expressão regular para números romanos válidos
    padraoComparacao = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    verificaRomano = bool(re.match(padraoComparacao, numero))
    if verificaRomano == False:
        print('\n')
        print("O valor inserido deve ser um número romano válido!")
        print('\n')
        exit()

match inputOption:
    case '1':
        print('\n')
        inputNumber = input("Digite um número real: ")
        verificaNumeroReal(inputNumber)
        real = Real(int(inputNumber))
        numeroConvertido = real.converteRealParaRomano()
        print('\n')
        print("Número romano: ",numeroConvertido)
        print('\n')
    case '2':
        print('\n')
        inputNumber = input("Digite um número romano: ")
        verificaNumeroRomano(inputNumber)
        romano = Romano(inputNumber)
        numeroConvertido = romano.converteRomanoParaReal()
        print('\n')
        print("Número real: ",numeroConvertido)
        print('\n')
    case '3':
       exit()  
    case _:
        print('\n')
        print("Opção não encontrada. ")
        print('\n')