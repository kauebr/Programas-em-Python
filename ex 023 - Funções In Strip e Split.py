# Criee um programa que identifique se uma pessoa nasceu numa cidade que começa com a palavra santo?
cid = str(input('Em que cidade você nasceu?:  '))
cid = cid.lower()
cid = cid.split()
print(cid)
print('santo' in cid[0])
print('-'*55)
end = input("digite seu endereço com logradouro, ex rua paulo, avenida maria: ")
end = end.strip()
print(end[:3].upper() == 'RUA')
print(end)