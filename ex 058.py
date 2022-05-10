from random import randint
from time import sleep
print('''
    \33[96m      ╔════•ೋೋ•════╗ 
    \33[93m        ...?Random!...
    \33[96m      ╚════•ೋೋ•════╝''')
sleep(1)
print('\33[93m            Sejem bem vinde!')
sleep(1)
print('\33[93m            Sei willkommen!')
sleep(1)
print('\33[93m                Salute!')
sleep(1)
print('\33[96m╔═════════════•ೋೋ•═════════════╗')
print('''  \33[93mFunciona assim, o computador vai 
  escolher um número de 0 a 10 e vc
  tem 10 tentativas para acertar!''')
print('\33[96m╚═════════════•ೋೋ•═════════════╝')
sleep(5)
flag0 = 0
flag1 = 0
npc = randint(0, 10)
print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
print('\33[93m   O computador está escolhendo', end='')
sleep(1)
print('\33[96m.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print('   Prontinho\33[93m!')
print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
sleep(1)
print('\33[93m   Agora é \33[96;4msua vez!\33[m')
acertou = False
erro = 1
tr = 10
while not acertou:
    print('   \33[93mTentativas restantes [\33[96m{}\33[93m]'.format(tr))
    if erro == 7:
        print('\33[91mVamos lá nao desista, você consegue')
    if erro == 10:
        print('   \33[91m :O Última chance!')
    pc = int(input('\33[93m   Escolha de \33[96m0 \33[93ma \33[96m10\33[93m: '))
    if erro == 10:
        print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
        print('   \33[91mNão foi dessa vez')
        print('   Você perdeu :(')
        acertou = True
    if pc == npc:
        acertou = True
        print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
        print('   \33[92;4mPARABÉNS VOCÊ \33[96;4mACERTOU\33[93;0m!\33[m')
        print('\33[93m   Tentativas realizadas: \33[96m{}'.format(erro))
        print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')

    else:
        print('   \33[96;1;41mErrou\33[m \33[93m[\33[91m{}\33[93m]'.format(erro))
        print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
    tr = tr - 1
    erro = erro +1

