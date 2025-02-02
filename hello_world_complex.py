from time import sleep
import emoji
message = 'Hello World!'
hw = str(input(emoji.emojize('Você quer rodar o Hello World :globo_mostrando_as_américas: [S/N]? ', language='pt'))).strip()[0]
while hw not in 'SsNn':
    hw = str(input('Valor inválido. Por favor use S ou N: '))
if hw in 'Ss':
    print('Você escolheu mostrar o ´Hello World!´...')
    sleep(1)
    print('Preparando a exibição da mensagem...')
    sleep(2)
    print('{}'.format(message))
elif hw in 'Nn':
    print('Você escolheu não exibir o ´Hello World!´...')
    sleep(1)
    print('Encerrando o programa...')
    sleep(2)
    print('Programa encerrado.')