from time import sleep

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['5', '10', '15', '25'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['2', '5', '10', '20'],
        'Resposta': '5'
    }
]

score = 0

for c, p in enumerate(perguntas):
    print(f'Pergunta n° {c+1}: {p["Pergunta"]}')
    print()
    print('Opções: ')
    options = p['Opções']
    for i, opc in enumerate(p['Opções']):
        print(f'{i}) {opc}')
        sleep(0.3)
    print()
    answer = input('Escolha uma opção: ')

    try:
        answer_int = int(answer)
    except ValueError:
        print('Opção inválida!')

    if options[answer_int] == p['Resposta']:
        print('Acertou! 🤘')
        score += 1
    else:
        print('Errou! ❌')
    print()
    sleep(1)

print(f'Você acertou {score} de 3 perguntas!')