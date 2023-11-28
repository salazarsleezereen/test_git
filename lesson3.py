'''
a = int(input("enter num: "))
if a > 0:
    print("polozhitelnoe chislo")
else:
    print("otritsatelnoe chislo")
'''

'''
chetnoe nechetnoe
a = int(input("enter num: "))
if a % 2 == 0:
    print("chetnoe chislo")
else:
    print("nechetnoe chislo")
'''
#sravnenie


'''
sravnenie i pokaz na skolko menshe
a = int(input("enter num: "))
b = int(input("enter num: "))

if a > b:
    print(f'{a} bolshe chem {b} na {a - b}')
else:
    print(f'{b} bolshe chem {a} na {b - a}')
'''
'''
a = int(input("enter num: "))

if a > 100:
    print("chislo bolshe chem 100")
elif a > 0:
    print("chislo bolshe 0")
'''

#calculator
'''
a = int(input("enter num: "))
b = int(input("enter num: "))
c = input("vyrazhenie ")

if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print(a/b)
else:
    print("vvedeno nekorrektnoe vyrazhenie")
'''
'''
a = int(input("enter login: "))
b = int(input("enter password: "))
c = int(input("repeat password: "))
if c==b:
    print("password matches")
elif c!=b:
    print("password does not match")
'''

'''
a = int(input("enter number: "))
b = int(input("enter number: "))

if a%b == 0:
    print('ok')
else:
    print('not ok')
'''
#vyvod bolshego chisla
'''
a = int(input("enter num: "))
b = int(input("enter num: "))
c = int(input("enter num: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
'''

'''first_num = int(input("enter first num: "))
second_num = int(input("enter second num: "))

a = input("vvedite chto vam nuzhno, slozheniw(s), vychutanie(v)")

if a =='S':
    print(first_num+second_num)
elif a == 'V':
    print(first_num - second_num)
else:
    print("vvedena nekorrektnaya bukva")'''






