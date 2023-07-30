# Palavra secreta
import os

word = "volume"
correct_letter = []
try_count = 0

while True:
    guess = input("Digite uma letra: ")
    
    if len(guess) > 1:
        print("Digite apenas uma letra cara!")
        continue

    try_count += 1

    if guess in word:
        correct_letter += guess

    show_word = ""

    for secret_letter in word:
        if secret_letter in correct_letter:
            show_word += secret_letter
        else:
            show_word += "*"

    print(show_word)

    if show_word == word:
        os.system('cls')
        print(f"VOCÊ ACERTOU A PALAVRA {word}!")
        print(f"Total de tentativas: {try_count}")
        break