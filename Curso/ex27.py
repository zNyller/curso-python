people = []
person = {}
total_age = average = 0

while True:
    person['name'] = input('Name: ')
    person['gender'] = input('Gender: ')
    person['age'] = int(input('Age: '))
    people.append(person.copy())
    next = input('Do you want to proceed? [Y]es/[N]o ').upper()[0]
    if next != 'N':
        continue
    break

print('-=' * 20)
print(f'O grupo tem {len(people)} pessoas.')
for p in people:
    total_age += p['age']
average = total_age / len(people)
print(f'A média de idade é de {average:.2f} anos.')
print(f'As mulheres cadastradas foram ', end=' ')
for p in people:
    if p['gender'] == 'F':
        print(p['name'], end='')

print('\nLista das pessoas que estão acima da média: ')
for p in people:
    if p['age'] > average:
        print(p)