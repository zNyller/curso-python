# King Dice

from random import randint
from time import sleep

game = {}

print('Valores sorteados:')
for c in range(0, 4):
    game[f'Player {c+1}'] = randint(1, 6)

for p, v in game.items():
    print(f'  O {p} tirou {v}')
    sleep(0.5)

print('Ranking dos jogadores:')
ranking = sorted(game.items(), key=lambda item: item[1], reverse=True)

for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
