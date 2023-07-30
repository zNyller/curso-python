# Detetive

def get_answers():
    questions = [
        'Telefonou para a vítima? ',
        'Esteve no local do crime? ',
        'Mora perto da vítima? ',
        'Devia para a vítima? ',
        'Já trabalhou com a vítima? '
    ]

    user_answers = []

    for question in questions:
        try:
            answer = input(question).upper()[0]
            while answer not in 'SN':
                print('Resposta inválida!')
                answer = input(question).upper()[0]
            else:
                user_answers.append(answer)
        except TypeError:
            print('Inválido!')

    return user_answers

def detective(answer_list):
    yes_count = answer_list.count('S')
    if yes_count == 5:
        print('Assassino(a)!')
    elif yes_count >= 3:
        print('Cúmplice!')
    elif yes_count == 2:
        print('Suspeito(a)!')
    else:
        print('Inocente!')

answers = get_answers()
print(answers)
detective(answers)