'''
def readInt(msg):
    ok = False
    value = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            value = int(num)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            return value

number = readInt('Digite um número: ')
print(f'Você acabou de digitar o número {number}')

'''
