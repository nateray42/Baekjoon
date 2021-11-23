#소수 구하기

n, m = map(int, input().split())
num_list = list(range(n, m+1))

a = [False,False] + [True]*m

primes=[]

for i in range(2,m+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, m+1, i):
        a[j] = False

for i in primes:
  if i >= n:
    print(i)