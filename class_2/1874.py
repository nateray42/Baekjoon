import sys
sys.stdin = open('input.txt')

num_list = [int(sys.stdin.readline()) for _ in range(int(input()))]

def solution(num_list):
  count = 0
  result = []
  stack = []
  while num_list:
    num = num_list.pop(0)
    while count < num:
      count += 1
      stack.append(count)
      result.append('+')
    if stack[-1] == num:
      stack.pop()
      result.append('-')
    else:
      return(print("NO"))
  for item in result:
    print(item)

solution(num_list)