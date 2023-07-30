# Funções

# Função com retorno -> Para utilizar o valor retornado em outra parte do código (Ex: uma variável)
def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplica_5_7_11 = multiplica(5, 7, 11)
print('*=' * 10)
print(multiplica_5_7_11)
print('*=' * 10)
print(5*7*11)

par_impar = int(input('Digite um número para ver se é par ou ímpar: '))
print(f'O número {par_impar} é par!') if par_impar % 2 == 0 else print(f'O número {par_impar} é ímpar!')

# Higher Order Functions 

def sayHy(msg, name):
    return f'{msg}, {name}!'

def execute(function, *args):
    return function(*args)

print(
    execute(sayHy, 'Bom dia', 'Edu')
)


# Funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Fallen', 'Art', 'Chelo']:
    print(falar_boa_noite(nome))

# =================================

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))