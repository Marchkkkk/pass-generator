import random

pas = ''
list = ('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ') ##list of symbols that will be used

passAmount = int (input('Ammount of passwords: '))
symbolsamount = int (input('Ammount of symbols: '))

f = open('resultpass.txt', 'w+')

for x in range(1, passAmount+1):

  for x in range(1, symbolsamount+1):
    pas = pas + random.choice(list)

  f.write(pas + '\n')
  pas =''
  
f.close()


