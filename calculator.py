from math import sqrt, factorial, pow, trunc
from time import sleep
from emoji import emojize

def StringFormatation(string = '', color = '', form = '', begin_form = 0, end_form = -1):
    color_code = ''
    form_code = ''
    if end_form == -1: end_form = len(string)

    if color == 'Cinza': color_code = '\033[30m'
    elif color == 'Vermelho': color_code = '\033[31m'
    elif color == 'Verde': color_code = '\033[32m'
    elif color == 'Amarelo': color_code =  '\033[33m'
    elif color == 'Azul': color_code = '\033[34m'
    elif color == 'Roxo': color_code = '\033[35m'
    elif color == 'Ciano': color_code = '\033[36m'
    elif color == 'Branco': color_code = '\033[37m'

    if form == 'Negrito': form_code = '\033[1m'
    elif form == 'Sublinhado': form_code = '\033[4m'
    elif form == 'Negativo': form_code = '\033[7m'

    clear_code = '\033[m'

    string = string.replace(string[begin_form:end_form + 1], color_code + form_code + string[begin_form:end_form + 1] + clear_code)
    return string

print(StringFormatation('-=' * 40, 'Amarelo', 'Negrito', 0))
print(f'{StringFormatation('  CALCULADORA DE TERMINAL  ', 'Azul', 'Negrito', 0):=^92}')
print(StringFormatation('=-' * 40, 'Amarelo', 'Negrito', 0))

sleep(1.5)
print(StringFormatation('\nBem vindo(a) à Calculadora!', 'Verde', 'Negrito', 0))
sleep(.5)
print(StringFormatation('Qual das operações a seguir deseja fazer? ', 'Cinza', 'Negrito'))
sleep(.5)

op = 0

ops = {
    1: "Adição",
    2: "Subtração",
    3: "Multiplicação",
    4: "Divisão",
    5: "Exponenciação (potência)",
    6: "Radiciação (raiz quadrada)",
    7: "Fatorial"
}
for pos, c in enumerate(ops):
    print(f'[{pos + 1}] {ops[c]}')
while op < 1 or op > 7:
    op = int(input())
    if op < 1 or op > 7:
        print(StringFormatation('Nenhuma operação válida. Tente novamente: ', 'Vermelho'))
print(StringFormatation(f'Você escolheu {ops[op]}', 'Azul', '', 14))
sleep(2)

v1 = 0
v2 = 0

if op in range(1, 5):
    action = ''
    if op == 1: action = 'somado'
    elif op == 2: action = 'subtraido'
    elif op == 3: action = 'multiplicado'
    elif op == 4: action = 'dividido'
    v1 = float(input(f'\nDigite o primeiro valor a ser {action}: '))
    v2 = float(input(f'Agora digite o segundo valor a ser {action}: '))
    while op == 4 and v2 == 0:
        v2 = float(input(StringFormatation('Não é possível dividir por 0. Tente outro número: ', 'Vermelho', '', 0, 28)))
elif op == 5:
    v1 = int(input('\nDigite qual será a base da potência: '))
    v2 = int(input('Agora digite qual será o expoente da potência: '))
elif op == 6:
    v1 = int(input('\nDigite o número no qual você quer saber a raiz quadrada: '))
elif op == 7:
    v1 = int(input('\nDigite o número no qual você quer fatorar: '))

if v1.is_integer(): v1 = trunc(v1)
if v2.is_integer(): v2 = trunc(v2)

print(StringFormatation('\nPROCESSANDO O CÁLCULO: ', 'Ciano', 'Negrito'))
sleep(2)

answer = 0
remainder = 0

print(StringFormatation(f'{'  RESPOSTA  ':=^80}', 'Verde', 'Negrito'))
complement = ''

if op == 1:
    answer = v1 + v2
    complement = f'da soma entre {v1} e {v2}'
elif op == 2:
    answer = v1 - v2
    complement = f'da subtração entre {v1} e {v2}'
elif op == 3:
    answer = v1 * v2
    complement = f'da multiplicação entre {v1} e {v2}'
elif op == 4:
    answer = v1 / v2
    remainder = v1 % v2
    complement = f'da divisão entre {v1} e {v2}'
elif op == 5:
    answer = pow(v1, v2)
    complement = f'do número {v1} elevado à {v2}ª potência'
elif op == 6:
    answer = sqrt(v1)
    complement = f'para a raiz quadrada de {v1}'
elif op == 7:
    answer = factorial(v1)
    complement = f'para o fatorial de {v1}'

print(StringFormatation(f'A resposta {complement} é:', 'Azul'))
print(trunc(answer) if answer.is_integer() else answer, end=', ' if op == 4 else '')
if op == 4: print(f'com resto da divisão igual à {remainder}.')
sleep(2)
