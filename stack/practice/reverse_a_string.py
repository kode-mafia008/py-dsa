# 1.Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
# Solution



from collections import deque


class StackReverse:

    def __init__(self):
        self.items = deque()
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
        self.items.append(item)
        self.size += 1

    def reverse(self, string):
        n = len(string)
        for i in range(0, n):
            self.items.append(string[i])

        string = ''

        for i in range(0, n):
            string += self.items.pop()

        return string


s = StackReverse()
# string = input('Enter String to be reversed: ')
result = s.reverse('I am vaccinated against COVID-19.')
print(result)
