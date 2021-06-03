from itertools import chain
n = int(input())
numbers = list(enumerate(map(int, input().split())))
numbers.sort(key=lambda x:x[1])
pairs = []
for i in range(len(numbers)-1) :
    current = numbers[i]
    if current[0] in chain.from_iterable(pairs): continue
    for j in range(i+1, len(numbers)):
        nex = numbers[j]
        if nex[0] in chain.from_iterable(pairs):
            continue
        if nex[1] == current[1]:
            pairs.append([current[0], nex[0]])
            break
print(len(pairs))
for a,b in pairs:
    print(a+1, b+1)
        
