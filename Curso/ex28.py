# Stats Players

team = []
player = {}
games = []

while True:
    player.clear()
    player['name'] = input('Player Name: ')
    total = int(input('How many games played? '))
    games.clear()
    for c in range(0, total):
        games.append(int(input(f'How many Kills in the {c+1}° game? ')))
    player['kills'] = games[:]
    team.append(player.copy())
    next = input('Wanto to Continue? [Y]es / [N]o: ').upper()[0]
    while next not in 'YN':
        next = input('Want to Continue? [Y]es / [N]o: ')
    if next == 'N':
        break

print('-=' * 20)

print(team)