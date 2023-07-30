# Hangman
from random import randint

words = [
    'Amarelo',
    'Amiga',
    'Amor',
    'Ave',
    'Avião',
    'Avó',
    'Balão',
    'Bebê',
    'Bolo',
    'Branco',
    'Cama',
    'Caneca',
    'Celular',
    'Céu',
    'Clube',
    'Copo',
    'Doce',
    'Elefante',
    'Escola',
    'Estojo',
    'Faca',
    'Foto',
    'Garfo',
    'Geleia',
    'Girafa',
    'Janela',
    'Limonada',
    'Mae',
    'Meia',
    'Noite',
    'Oculos',
    'Onibus',
    'Ovo',
    'Pai',
    'Parque',
    'Passarinho',
    'Peixe',
    'Pijama',
    'Rato',
    'Umbigo'
]

words = [word.upper() for word in words]

index = randint(0, 39)
secret_word = words[index]

max_attempts = 7
attempts = 0
correct_letter = set()

# Hangman stages
hangman_stages = [
    '''
       _______
      |       |
      |       
      |      
      |     
      |     
      |
    _|___
    ''',
    '''
       _______
      |       |
      |       O
      |      
      |     
      |     
      |
    _|___
    ''',
    '''
       _______
      |       |
      |       O
      |       |
      |       |
      |      
      |
    _|___
    ''',
    '''
       _______
      |       |
      |       O
      |      /|
      |       |
      |      
      |
    _|___
    ''',
    '''
       _______
      |       |
      |       O
      |      /|\\
      |       |
      |      
      |
    _|___
    ''',
    '''
       _______
      |       |
      |       O
      |      /|\\
      |       |
      |      /
      |
    _|___
    ''',
    '''
       _______
      |       |
      |       O
      |      /|\\
      |       |
      |      / 
      |
    _|___
    ''',
    '''
       _______
      |       |
      |       O
      |      /|\\
      |       |
      |      / \\
      |
    _|___
    '''
]

print(f'Adivinhe a palavra: ', '*' * len(secret_word))

while True:
    guess = input('Digite uma letra: ').upper()
    if guess in secret_word:
        correct_letter.add(guess)
    else:
        attempts += 1
        print(f'Tentativas restantes: {max_attempts - attempts}')

    show_word = ''.join([letter if letter in correct_letter else '*' for letter in secret_word])

    print(show_word)

    if attempts == max_attempts:
        print('Que pena! Você foi de base!')
        print(f'A palavra era: {secret_word}')
        print(hangman_stages[attempts])
        break

    if show_word == secret_word:
        print('PARABÉNS!')
        break

    print(hangman_stages[attempts])