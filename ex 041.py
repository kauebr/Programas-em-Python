print('\33[97m-'*33)
ag = int(input('Please, type your age here: '))
if ag <= 9:
    print("Mirin Class's")
elif ag > 9 and ag <= 14:
    print("Children's class")
elif ag > 14 and ag <= 19:
    print("Junior's Class")
elif ag > 19 and ag <= 20:
    print("Senior's Class")
else:
    print("Master's Class")
print('\33[97m-'*33)


