# Lista de compras

import os

shop_list = []

while True:
    option = input("Selecione uma opção \n[i]nserir [a]pagar [l]istar: ")

    if option == 'i':
        os.system('cls')
        item = input("Selecione o produto: ")
        shop_list.append(item)
        print("Ítem adicionado!")

    elif option == 'a':
        try:
            delete_item = int(input("Escolha o índice para apagar: "))
            shop_list.pop(delete_item)
            print("Ítem removido!")
        except ValueError:
            print("Por favor, digite um número inteiro.")
        except IndexError:
            print("Índice não existe na lista!")
        except Exception:
            print("Erro desconhecido!")

    elif option == 'l':
        if len(shop_list) < 1:
            print("Sua lista de compras está vazia!")
        else:
            os.system('cls')
            print(f"Sua lista de compras: ")
            for i, product in enumerate(shop_list):
                print(f"[{i}]", product)
        
    else:
        print("Opção inválida!")
        continue