import sys
import collections


sys.stdin = open("input.txt", "r") 
input_list = collections.deque()

for line in sys.stdin:
    new_list = [int(elem) for elem in line.split()]
    input_list.append(new_list)

iter_num = int(input_list.popleft()[0])

for item in sorted(input_list):
  print(item[0], item[1])