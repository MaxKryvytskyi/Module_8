from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)

element = ["Bob", "Nick"]

def push(element):
    return fifo.append(element)

def pop():
    return fifo.popleft()

print(push(element))
print(pop())