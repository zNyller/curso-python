nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome == "":
    print("Digite um nome válido")

elif idade == "":
    print("Digite uma idade válida!")

else:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome tem {len(nome)} letras.")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)