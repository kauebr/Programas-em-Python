from time import  sleep
import emoji
print('\33[91m{}{}'.format('-='*4, '-'))
sleep(1)
for c in range(10, -1 , -1):
    print('{}{}{}'.format('...', c, '...'))
    sleep(1)
print(emoji.emojize('\33[93m:collision: VIVA!! :collision:', use_aliases=True))

pip install emoji()