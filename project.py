from random import randint, shuffle

"""trees = ['M','M','M','O','O','O','O','B','B','B','B','B']

failures=0
trials=100

for i in range(trials):
    shuffle(trees)
    #print(trees)
    for j in range(9):
        if trees[j] == 'B' and trees[j+1] == 'B' and trees[j+2] == 'B' and trees[j+3] == 'B':
            #print("fail")
            failures += 1
            break

print((trials-failures)/trials, '%')

trial=10000
heads=0

for i in range(trial):
    if randint(0,1)==1:
        heads+=1
print(heads)"""

die=[0,0,0,0,0]

while 0 in die:
    rand=randint(0,5)
    