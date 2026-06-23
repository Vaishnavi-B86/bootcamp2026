def maximum(a, b):
    if a > b:
        return a
    else:
        return b

a, b = map(int, input().split())
print(maximum(a, b))
