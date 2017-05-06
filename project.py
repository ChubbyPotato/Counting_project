from random import randint, shuffle

#"""
#1
cards=['q','q','q','q','k','k','k','k','j','j','j','j']
trials=10
ya=0

for i in range(trials):
    shuffle(cards)
    for x in range(len(cards)-1):
        if cards[x] =='q' and cards[x+1] == 'q' and cards[x+2] == 'q' and cards[x+3] == 'q':
            ya+=1
        elif cards[x] =='k' and cards[x+1] == 'k' and cards[x+2] == 'k' and cards[x+3] == 'k':
            ya+=1
        elif cards[x] =='j' and cards[x+1] == 'j' and cards[x+2] == 'j' and cards[x+3] == 'j':
            ya+=1
        else:
            break

print(100*ya/trials, '%')
#"""
#"""
#2
trials2=10
c=['c']
b=['t','t1','t2']
lis=12*c+b
yas=0

for i in range(trials2):
    shuffle(lis);
    t= lis.index('t')
    t1= lis.index('t1')
    t2= lis.index('t2')
    for j in range(trials2):
        if t == 0 or t1 == 0 or t2 == 0:
            yas+=0
            break
        elif t == 14 or t1 == 14 or t2 == 14:
            yas+=0
            break
        else:
            if lis[t-1] == 'c' and lis[t+1]:
                if lis[t1-1] == 'c' and lis[t1+1]:
                    if lis[t2-1] == 'c' and lis[t2+1]:
                        yas+= 1
                        break
                    else:
                        break
                else:
                    break
            else:
                break
                
print("Probability of getting at least 2 students on either side of teacher:", 100*yas/trials2,"%")
#"""
#"""
#3

sib=['s1','s2','s3','s4','s5']*2
trials3= 10
yee=0

for i in range(trials3):
    shuffle(sib)
    for j in range(len(sib)-1):
        if sib[j] == sib[j+1]:
            yee+=1;

print("Average number of pairs of siblings sitting together:", yee/trials3)
#"""