# 2.Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True


from collections import deque


class CheckStack:

    def __init__(self):
        self.stack = deque()
        self.size = -1

    def isEmpty(self):
        if (self.size == -1):
            return True
        else:
            return False

    def pop(self):
        if (self.isEmpty):
            print('Stack is empty')
        else:
            self.size -= 1

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def size(self):
        return len(self.stack)

    def is_match(char1, char2):
        match_dict = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        return match_dict[char1] == char2

    def check_brackets_balance(self, string):
        stack = CheckStack()
        for char in string:
            if char in ["(", "{", "["]:
                stack.push(char)
            else:
                if char in ["}", ")", "]"]:
                    if stack.size() == 0:
                        return False
                    if not stack.is_match(char, stack.pop()):
                        return False
        return stack.size() == 0


s = CheckStack()
expr = "[][]()[{"

print(s.check_brackets_balance(expr))
