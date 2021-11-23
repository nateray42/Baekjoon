#소수 찾기

n = int(input())
inputs = input().split(' ')
inputs = [int(x) for x in inputs]
if 1 in inputs:
    inputs.remove(1)
else:
    pass


num_of_prime = 0

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1

for item in inputs:
    num_of_prime += is_prime(item)

print(num_of_prime)