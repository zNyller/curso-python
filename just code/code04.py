from time import sleep
import random

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        sleep(0.03)
    print()

def introduction():
    print_slow("Você acorda em uma praia. O sol está nascendo e você se encontra em uma ilha misteriosa.")
    print_slow("Você não tem memória de como chegou aqui. Seu objetivo é encontrar uma maneira de sair da ilha.")
    print_slow("Você vê uma selva à sua esquerda e uma densa floresta à sua direita.")
    print_slow("O que você quer fazer?\n")

def explore_jungle():
    print_slow("Você se aventura na selva.")
    
    print_slow("Conforme você avança pela vegetação densa, você dá de cara com um animal selvagem!")

    # Implement a choice for the player to interact with the animal
    while True:
        choice = input("Você (A)taca ou (C)orre para longe? ").lower()
        if choice == 'a':
            print_slow("Você decidiu atacar o animal!")
            # Determine the outcome of the attack using random chance
            attack_success = random.random() < 0.5  # 50% chance of success

            if attack_success:
                print_slow("Seu ataque deu certo! O animal foge para longe, assustado com sua demonstração de força.")
            else:
                print_slow("Seu ataque falha, e o animal contra-ataca.")
                print_slow("Você está um pouco machucado, mas consegue assustar o animal para longe.")

            break
        elif choice == 'c':
            print_slow("Você decidiu correr para longe do animal.")
            # Determine the outcome of running away using random chance
            escape_success = random.random() < 0.8  # 80% chance of success

            if escape_success:
                print_slow("Você consegue escapar do animal e seguir explorando a selva.")
            else:
                print_slow("O animal lhe persegue por um tempo, mas você encontra um local seguro para se esconder.")
                print_slow("Depois de algum tempo, o animal perde o interesse e vai embora.")

            break
        else:
            print_slow("Opção inválida! Tente novamente.")

    # After dealing with the animal, continue the jungle exploration
    print_slow("Enquanto explora mais, você encontra um templo de pedra muito antigo.")

    # Implement a choice for the player to enter the temple or keep exploring
    while True:
        choice = input("Você [E]ntra no Templo ou [C]ontinua explorando a selva? ").lower()
        if choice == 'e':
            print_slow("Você decide entrar no templo.")
            print_slow("Dentro do templo, você encontra artefatos antigos e tesouros valiosos.")
            print_slow("Você sente que está chegando perto de descobrir os mistérios da ilha.")
            break
        elif choice == 'c':
            print_slow("Você decide continuar explorando a selva.")
            print_slow("Você descobre uma cachoeira escondida e uma caverna atrás dela.")
            break
        else:
            print_slow("Opção inválida! Tente novamente.")

    print_slow("Você encontra um baú de tesouro escondido. Está trancado. Continue explorando para encontrar uma chave.")

def explore_forest():
    print_slow("Você se aventura na floresta densa.")
    # Implement forest exploration logic here
    print_slow("Você se depara com uma cabana abandonada. Procure dentro por pistas.")

def explore_hut():
    print_slow("Dentro da cabana, você encontra um velho diário empoeirado e uma chave enferrujada.")
    # Implement hut exploration logic here
    print_slow("Você decide levar o diário e a chave com você.")

def unlock_chest():
    print_slow("Você usa a chave enferrujada para abrir o baú do tesouro.")
        # Determine the outcome of unlocking the chest using random chance
    unlock_success = random.random() < 0.7  # 70% chance of success

    if unlock_success:
        print_slow("Parabéns! Você conseguiu destrancar o baú.")
        print_slow("Você encontra um mapa que mostra a saída da ilha.")
        print_slow("Você segue o mapa e finalmente escapa da ilha misteriosa. Muito bem!")
    else:
        print_slow("A chave quebra enquanto você tentava abrir o baú.")
        print_slow("Você ouve um click, e o baú parece estar preso.")
        print_slow("Você decide se afastar, e o baú permanece trancado.")
        print_slow("Talvez o mapa esteja perdido para sempre, mas você continua sua jornada para achar outra maneira de sair da ilha.")

def game_over():
    print_slow("GAME OVER")
    print_slow("Obrigado por jogar!")

def play_game():
    introduction()
    
    while True:
        key = 0
        user_input = input("> ").lower()

        if "selva" in user_input:
            explore_jungle()
        elif "floresta" in user_input:
            explore_forest()
        elif "cabana" in user_input:
            explore_hut()
            key = 1
        elif "chave" in user_input:
            if key == 1:
                unlock_chest()
                break
            else:
                print_slow("Você ainda não encontrou nenhuma chave.")
        else:
            print_slow("Comando inválido. Tente novamente.")

    game_over()

if __name__ == "__main__":
    play_game()