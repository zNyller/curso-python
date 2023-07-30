from datetime import date
person = {}
current_year = date.today().year
person['name'] = input('Nome: ')
person['age'] = current_year - int(input('Ano de nascimento: '))
person['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if person['ctps'] != 0:
    person['sign'] = int(input('Ano de contratação: '))
    person['salary'] = float(input('Salário: '))
    person['retirement'] = (person['sign'] + 35) - (current_year - person['age'])
print('-=' * 20)
for k, v in person.items():
    print(f'{k} tem o valor {v}')