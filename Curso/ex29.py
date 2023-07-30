def notas(*grades, sit=False):
    nota = {}
    nota['total'] = len(grades)
    nota['maior'] = max(grades)
    nota['menor'] = min(grades)
    nota['media'] = sum(grades) / len(grades)
    if sit:
        if nota['media'] >= 7:
            nota['situacao'] = 'BOA!'
        elif nota['media'] > 5:
            nota['situacao'] = 'RAZOÁVEL!'
        else:
            nota['situacao'] = 'RUIM!'
    return nota

resp = notas(9.5, 8, 6.5, 2, 7.2, 5, sit=True)
print(resp)