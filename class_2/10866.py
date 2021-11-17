import sys
import collections

sys.stdin = open("input.txt", "r") 
dlist = collections.deque()

for line in sys.stdin:
    new_list = [elem for elem in line.split()]
    dlist.append(new_list)

iter_num = int(dlist.popleft()[0])

stack = collections.deque()

def do_push_front(dlist):
  stack.append(int(dlist[1]))

def do_push_back(dlist):
  stack.appendleft(int(dlist[1]))

def do_pop_front(dlist):
  try:
    print(stack.pop())
  except:
    print(-1)

def do_pop_back(dlist):
  try:
    print(stack.popleft())
  except:
    print(-1)

def do_size(dlist):
  print(len(stack))

def do_empty(dlist):
  if len(stack) == 0:
    print(1)
  else:
    print(0)

def do_front(dlist):
  try:
    print(stack[-1])
  except:
    print(-1)

def do_back(dlist):
  try:
    print(stack[0])
  except:
    print(-1)

  
command = {
  "push_front": do_push_front,
  "push_back": do_push_back,
  "pop_front": do_pop_front,
  "pop_back": do_pop_back,
  "size": do_size,
  "empty": do_empty,
  "front": do_front,
  "back": do_back
}

for i in range(iter_num):
  command[dlist[i][0]](dlist[i])