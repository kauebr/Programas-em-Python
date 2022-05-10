
#:fist: pedra :Facepunch:
#:wave: pel'''
#:v: tesoura
from emoji import emojize
from random import randint
from time import sleep
c = 0
print(emojize('by KCODE \33[96m:thumbs_up:'))
sleep(0.3)
print('\33[95m=\33[96m=' * 20)
sleep(0.3)
print('{:=^40}'.format('JO KEN PO!'))
sleep(0.3)
print('\33[95m=\33[96m=' * 20)
while c < 4:
    c = c + 1
    sleep(0.3)
    print(emojize('\33[95m[1] \33[93m:fist:', use_aliases=True))
    sleep(0.3)
    print(emojize('\33[95m[3] \33[93m:wave:', use_aliases=True))
    sleep(0.3)
    print(emojize('\33[95m[2] \33[93m:v:', use_aliases=True))
    npc = int(input('\33[96m ESCOLHA: '))
    sleep(0.3)
    pc = randint(1, 3)
    print('\33[95m=\33[96m='*20)
    print('\33[93mJO', end='')
    sleep(0.3)
    print('\33[96m...')
    sleep(0.3)
    print('\33[93mKEN', end='')
    sleep(0.3)
    print('\33[96m...')
    sleep(1)
    print('\33[93mPÔ\33[96m!')
    print('\33[95m=\33[96m='*20)
    if npc == 1 and pc == 1:
        print(emojize('   VOCÈ:    \33[93m:facepunch:', use_aliases=True))
        print(emojize('\33[96mCOMPUTADOR: \33[93m:facepunch:', use_aliases=True))
        print('\33[93m  EMPATOU!')
    elif npc == 1 and pc == 2:
        print(emojize('   VOCÈ:    \33[93m:facepunch:', use_aliases=True))
        print(emojize('\33[96mCOMPUTADOR: \33[93m:wave:', use_aliases=True))
        print('\33[91mVOCÊ PERDEU!')
        print(emojize('\33[97mEu nunca fiquei tao triste \33[91m:broken_heart:', use_aliases=True))
    elif npc == 1 and pc == 3:
        print(emojize('   VOCÈ:    \33[93m:facepunch:', use_aliases=True))
        print(emojize('\33[96mCOMPUTADOR: \33[93m:v:', use_aliases=True))
        print('\33[92mVOCÊ GANHOU!')
        sleep(0.3)
        print(emojize('\33[36m PARABÉNS! \33[33m:smile:', use_aliases=True))
    elif npc == 2 and pc == 1:
        print(emojize('   VOCÈ:    \33[93m:wave:', use_aliases=True))
        print(emojize('\33[96mCOMPUTADOR: \33[93m:facepunch:', use_aliases=True))
        print('\33[92mVOCÊ GANHOU!')
        sleep(0.3)
        print(emojize('\33[36m PARABÉNS! \33[33m:smile:', use_aliases=True))
    elif npc == 2 and pc == 2:
        print(emojize('   VOCÈ:    \33[93m:wave:', use_aliases=True))
        print(emojize('\33[96mCOMPUTADOR: \33[93m:wave:', use_aliases=True))
        print('\33[93m  EMPATOU!')
    elif npc ==2 and pc == 3:
        print(emojize('   VOCÈ:    \33[93m:wave:', use_aliases=True))
        print(emojize('\33[96mCOMPUTADOR: \33[93m:v:', use_aliases=True))
        print('\33[91mVOCÊ PERDEU!')
        print(emojize('\33[97mEu nunca fiquei tao triste \33[91m:broken_heart:', use_aliases=True))
    elif npc == 3 and pc == 1:
        print(emojize('   VOCÈ:    \33[93m:v:', use_aliases=True))
        print(emojize('\33[96mCOMPUTADOR: \33[93m:facepunch:', use_aliases=True))
        print('\33[91mVOCÊ PERDEU!')
        print(emojize('\33[97mEu nunca fiquei tao triste \33[91m:broken_heart:', use_aliases=True))
    elif npc == 3 and pc == 2:
        print(emojize('   VOCÈ:    \33[93m:v:', use_aliases=True))
        print(emojize('\33[96mCOMPUTADOR: \33[93m:wave:', use_aliases=True))
        print('\33[92mVOCÊ GANHOU!')
        sleep(0.3)
        print(emojize('\33[36m PARABÉNS! \33[33m:smile:', use_aliases=True))
    else:
        print(emojize('   VOCÈ:    \33[93m:v:', use_aliases=True))
        print(emojize('\33[96mCOMPUTADOR: \33[93m:v:', use_aliases=True))
        print('\33[93m  EMPATOU!')
    sleep(0.3)
    print('\33[95m=\33[96m='*20)