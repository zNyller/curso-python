def stats(player='<unknown>', goals = 0):
    print(f'O jogador {player} fez {goals} gol(s) no campeonato!')

name = input('Nome do jogador: ')
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if name.strip() == '':
    stats(goals=gols)
else:
    stats(name, gols)
