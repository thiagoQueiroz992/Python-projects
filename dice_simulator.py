from random import randint
from time import sleep
from emoji import emojize#, LANGUAGES

emojis = {
    'dado': ':jogo_de_dado:'
}
colors = {
    "negrito_e_amarelo": "\033[1;33m",
    "negrito_e_ciano": "\033[1;36m",
    "negrito_e_roxo": "\033[1;35m",
    "negrito_e_azul": "\033[1;34m",
    "vermelho": "\033[31m",
    "limpar": "\033[m",

}
print(emojize(f'{emojis['dado']} {colors["negrito_e_amarelo"]}SIMULADOR DE DADOS DE TERMINAL{colors["limpar"]} {emojis['dado']}\n', language='pt'))
while True:
    dice_quant = int(input(f'Quantos dados você quer lançar, {colors["negrito_e_azul"]}1 ou 2?{colors["limpar"]} '))
    if dice_quant != 1 and dice_quant != 2:
        print(emojize(f'{colors["vermelho"]}Só é possível jogar 1 ou 2 dados! {emojis['dado'] * 2}{colors["limpar"]}\n', language='pt'))
        continue
    print(f'\n{colors["negrito_e_ciano"]}ARREMESSANDO {'O DADO' if dice_quant == 1 else 'OS DADOS'}...{colors["limpar"]}')
    sleep(1)

    for c in range(0, 5):
        print(emojize(f'{emojis['dado']}', language='pt'))
        sleep(1)
    dice_value_1 = randint(1, 6)
    if dice_quant == 1:
        print(emojize(f'{emojis['dado']} O dado foi lançado com a face {colors["negrito_e_roxo"] + str(dice_value_1) + colors["limpar"]} virada para cima!', language='pt'))
    else:
        dice_value_2 = randint(1, 6)
        print(f'O primeiro dado foi lançado com a face {colors["negrito_e_roxo"] + str(dice_value_1) + colors["limpar"]} virada para cima e o segundo dado foi lançado com a face {colors["negrito_e_roxo"] + str(dice_value_2) + colors["limpar"]} virada para cima.')
        print(emojize(f'{emojis['dado']} O total de pontos obtidos através desses dois dados foi de {colors["negrito_e_roxo"] + str(dice_value_1 + dice_value_2) + colors["limpar"]}.', language='pt'))
    cont = 'null'
    sleep(1.5)
    while cont not in 'SsNn':
        cont = str(input(emojize(f'\nDeseja continuar jogando {emojis['dado']}? {colors["negrito_e_azul"]}S [sim], N [não].{colors["limpar"]} ', language='pt'))).strip()[0]
    if cont in 'Ss': continue
    else: break
print(f'\n{colors["negrito_e_ciano"]}JOGO DE DADOS ENCERRADO!{colors["limpar"]}')
