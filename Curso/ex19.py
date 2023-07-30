def voto(year):
    from datetime import date
    current = date.today().year
    age = current - year
    if age >= 18:
        return f'Com {age} anos: VOTO OBRIGATÓRIO!'
    elif age >= 16 and age < 18:
        return f'Com {age} anos: VOTO OPCIONAL!'
    return f'Com {age} anos: NÃO VOTA!'

print('-' * 20)
user = int(input("Em que ano você nasceu? "))
print(voto(user))