from random import randint
npc = randint(0,10)
print('Sou seu computador, acabei de pensar no número entre 0 e 10.')
print('Será que você consegue acertar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpites += 1
    if jogador == npc:
        acertou = True
    if palpites == 10:
        acertou = True
    if acertou == True:
        print('Acertou com {} palpites'.format(palpites))


from random import randint
from time import sleep

flag0 = 1  # Flag responsável pelo 'Restart" do jogo
flag1 = 1  # Flag deseja continuar
reset = 'x'# Flag deseja continuar
y = 1  # timer
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
sleep(y)
print('\33[96m.', end='')
sleep(y)
print('.', end='')
sleep(y)
print('.')
sleep(y)
print('   Prontinho\33[93m!')
print(npc)
print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
sleep(y)
print('\33[93m   Agora é \33[96;4msua vez!\33[m')
c = 0  # contador
pc = -1  # escolha do player
cp = 10  # contador de pontos
erro = 0
while : #repeticao de escolhas do usuário
     print('C: {}'.format(c))
     if pc == npc:
        print('   \33[92;4mPARABÉNS VOCÊ \33[96;4mACERTOU\33[93;0m!\33[m')
        print('\33[93m   Tentativas realizadas: \33[96m{}'.format(erro))
        print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
        flag1 = 1
        active = False
     if cp == 1:  #contador de ponto
       flag0 = 1
       if npc == pc:
          flag0 = 1
     print('   \33[93mTentativas restantes [\33[96m{}\33[93m]'.format(cp))
     pc = int(input('\33[93m   Escolha de \33[96m0 \33[93ma \33[96m10\33[93m: '))
     cp -= 1
    if pc > 10 and pc:
       print('\33[91mVocê tem que escolher um número entre 0 e 10')
       if pc != npc:
          erro += 1
          c += 1
          print('   \33[96;1;41mErrou\33[m \33[93m[\33[91m{}\33[93m]'.format(erro))
      if pc != npc and cp == 3:
        print('\33[91mVamos lá nao desista, você consegue')
      if pc != npc and cp == 1:
         print('   \33[91m :O Última chance!')
         print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
       else:
        print('   \33[91mNão foi dessa vez')
        print('   Você perdeu :(')
sleep(1)
print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
print('\33[93mObrigado por jogar até a proxima \33[96m=)\33[93m!')
print('\33[93m•\33[96m═══════════════════════════════════\33[93m•')
