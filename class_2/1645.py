import sys

dlist = []
sys.stdin = open("input.txt", "r") 

for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    dlist.append(new_list)

k, n = map(int, dlist.pop(0))

dlist = sorted(dlist)
dlist = [x[0] for x in dlist]

first, last = 1, max(dlist)
while first <= last:
    mid = (first + last) // 2
    num = 0
    for item in dlist:
      num += (item // mid)
    if num < n: 
      last = mid - 1
    else: 
      first = mid + 1

print(last)


