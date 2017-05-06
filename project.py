from random import randint, shuffle
"""
cards=['q','q','q','q','k','k','k','k','j','j','j','j']
cardlen= len(cards)-1
trials=10
ya=0

for i in range(trials):
    shuffle(cards)
    for x in range(cardlen):
        if cards[x] =='q' and cards[x+1] == 'q' and cards[x+2] == 'q' and cards[x+3] == 'q':
            ya+=1
        elif cards[x] =='k' and cards[x+1] == 'k' and cards[x+2] == 'k' and cards[x+3] == 'k':
            ya+=1
        elif cards[x] =='j' and cards[x+1] == 'j' and cards[x+2] == 'j' and cards[x+3] == 'j':
            ya+=1
        else:
            break
    
print(ya)
print(100*ya/trials, '%')
"""

trials2=5

c=['c']
b=['t','t1','t2']
lis=12*c+b
lislen=len(lis)-1
yas=0

for i in range(trials2):
    shuffle(lis);
    for j in range(lislen):
        if lis[j] == 'c' and lis[j+1] == 't' and lis[j+2] == "c":
            print(True)
        elif lis[j] == 'c' and lis[j+1] == 't1' and lis[j+2] == "c":
            print(True)
        elif lis[j] == 'c' and lis[j+1] == 't2' and lis[j+2] == "c":
            print(True)
        else:
            print(False)
            break
        
        