# Artilheiro

player ={}
goals = []

player['name'] = input('Nome do Jogador: ')
games = int(input(f'Quantas partidas {player["name"]} jogou? '))

for c in range(0, games):
    goals.append(int(input(f'Quantos gols na partida {c}? ')))
    
player['goals'] = goals
player['total_goals'] = sum(goals)
print(player)

print('-=' * 20)

for k, v in player.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 20)

player['games'] = games

print(f'O jogador {player["name"]} jogou {player["games"]} partidas.')
for g, go in enumerate(player['goals']):
    print(f'   -> Na partida {g}, fez {go} gols.')
print(f'Foi um total de {player["total_goals"]} gols.')