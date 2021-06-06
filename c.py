n=6
A = [1]
for i in range(n, 1, -1):
    A.append(A[-1] * i)
A.append(1)
print(A)