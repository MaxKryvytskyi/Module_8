

from collections import deque

MAX_LEN = 5

lifo = deque(maxlen=MAX_LEN)

element = ["Bob", "Nick"]

def push(element):
    lifo.appendleft(element)

def pop():
    return lifo.popleft()

print(push(element))
print(pop())
    
    