from itertools import permutations

s, k = input().split()
k = int(k)

s = sorted(s)
p = permutations(s, k)

for i in p:
    print(''.join(i))
    