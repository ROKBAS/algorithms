n = 10

print("O(n^2)")

for i in range (0,n):
    for j in range (0,n):
        print(i,j)

print("O(n^2)")

for i in range(0,n):
    for j in range(0,j):
        print(i,j)

print("O(sqrt(N))")

i = 1
while i*i<n:
    print(i)
    i+=1

print("O(log2n)")

i = 1
while i<n:
    i*=2
    print(i)

print("O(n)")

def f(n):
    if n==0:
        print("0 - zero")
    else:
        print(n)
        f(n-1)

f(n)

print("O(logn)")

def f2(n):
    if n==0:
        print("0 - zero")
    else:
        f2(n//2)
        f2(n//2)
f2(n)


