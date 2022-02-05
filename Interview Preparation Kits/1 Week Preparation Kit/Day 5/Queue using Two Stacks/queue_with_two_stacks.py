#!/usr/bin/env python3

class Queue:
    def __init__(self, stack1=[], stack2=[]):
        self.stack1 = stack1
        self.stack2 = stack2

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def first(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


if __name__ == '__main__':
    test_cases = int(input().strip())
    q = Queue()

    for t in range(test_cases):
        action = input()

        if action[0] == "1":
            data = action.split(" ")[1]
            q.enqueue(data)
        elif action[0] == "2":
            q.dequeue()
        else:
            print(q.first())

