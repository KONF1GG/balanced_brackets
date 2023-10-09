
class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def is_balanced(subsequence):
    stack = Stack()

    brackets = {')': '(', ']': '[', '}': '{'}

    for char in subsequence:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.peek() != brackets[char]:
                return 'Несбалансированно'
            else:
                stack.pop()

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"



print(is_balanced(('[[{())}]')))