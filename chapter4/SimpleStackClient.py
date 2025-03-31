from SimpleStack import *

stack = Stack(10)

for word in ['I', 'love', 'python']:
    stack.push(word)

print('After pushing ', len(stack), 'words on the stack, it contains:\n', stack)

print('Is stack full?', stack.isFull())

print('Popping items off the stack:')

while not stack.isEmpty():
    print(stack.pop(), end=' ')

print()