from random import randint, shuffle

trees = ['M','M','M','O','O','O','O','B','B','B','B','B']

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