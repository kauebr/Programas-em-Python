try: # tente isso
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b

except Exception as erro: # se der errado retorne isso
    print(f'Infelizmente tivemos o erro "{erro.__class__}"')
else: # se der certo retorne isso
    print(f'O resultado é {r:.1f}')
finally: # Por fim, independende do condicional acima retorne isto
    print('Volte Sempre')

tipos_de_erro = ('TypeError, ValueError', 'ZeroDivisionError',)