N = 23
X = [i - 10 + N for i in range(20)]
print(X)
M = 7
Y = [elem for elem in X if abs(elem) > M]
print(M)
print(Y)