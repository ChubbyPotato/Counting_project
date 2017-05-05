from random import randint, shuffle

trees = ['M','M','M','O','O','O','O','B','B','B','B','B']

failures=0
trials=10

for i in range(trials):
    shuffle(trees)
    print(trees)
    for j in range(trials-1):
        if trees[j] == 'B' and trees[j+1] == 'B' and trees[j+2] == 'B' and trees[j+3] == 'B':
            print("fail")
            failures += 1
            break

print(failures)