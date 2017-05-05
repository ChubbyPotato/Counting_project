from random import randint, shuffle

cards=['q','q','q','q','k','k','k','k','j','j','j','j']
trials=10000
ya=0

for i in range(trials):
    shuffle(cards)
    for x in range(0,11):
        if cards[x] =='q' and cards[x+1] == 'q' and cards[x+2] == 'q' and cards[x+3] == 'q':
            ya+=1
            break
        elif cards[x] =='k' and cards[x+1] == 'k' and cards[x+2] == 'k' and cards[x+3] == 'k':
            ya+=1
            break
        elif cards[x] =='j' and cards[x+1] == 'j' and cards[x+2] == 'j' and cards[x+3] == 'j':
            ya+=1
            break
        else:
            break
print(ya)
