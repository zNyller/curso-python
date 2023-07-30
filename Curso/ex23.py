# Média Notas

student = {}

student['name'] = input('Nome: ')
student['average'] = float(input(f'Média de {student["name"]}: '))

if student['average'] < 6:
    student['situation'] = 'Reprovado'
else:
    student['situation'] = 'Aprovado'

print(f'Nome é igual a {student["name"]}')
print(f'Média é igual a {student["average"]}')
print(f'Situação é igual a {student["situation"]}!')