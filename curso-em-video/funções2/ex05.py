def notas(*notas, sit=None):
    obj = dict()
    obj['quantidade'] = len(notas)
    obj['maiornota'] = max(notas)
    obj['menornota'] = min(notas)
    obj['media'] = sum(notas)/len(notas)
    if sit:
        if obj['media'] > 8:
            obj['situacao'] = 'Ótima'
        elif obj['media'] > 6:
            obj['situacao'] = 'Boa'
        else:
            obj['situacao'] = 'Preocupante'
    return obj


resp = notas(5.5, 2.5, 1.5, sit=True)
print('-'*40)
print(resp)
