while True:
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    operador = input("Digite um operador(+-*/): ")

    if num1.isdigit() and num2.isdigit():

        num1_int = int(num1)
        num2_int = int(num2)

        if operador == "+":
            print(f"Resultado: {num1_int + num2_int}")

        elif operador == "-":
            print(f"Resultado: {num1_int - num2_int}")

        elif operador == "*":
            print(f"Resultado: {num1_int * num2_int}")

        elif operador == "/":
            print(f"Resultado: {num1_int / num2_int}")

        else:
            print("Operador inválido!")
    else:
        print("Digite um número valido!")
        continue



    sair = input ("Você deseja sair? [s]im: ").lower().startswith('s')
    if sair:
        print("Bye!")
        break


frase = "O Python é uma linguagem de programação"

print(frase.count('Python'))