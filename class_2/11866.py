import collections

k, n = map(int, input().split(' '))

circle = collections.deque(range(1, k+1))
circle_list = []

while len(circle) != 0:
  circle.rotate(-n)
  circle_list.append(circle.pop())

print(str(circle_list).replace('[', '<').replace(']', '>'))
