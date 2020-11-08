class MyQueue(object):
    def __init__(self):
        self.enqueue = []
        self.dequeue = []
    
    def peek(self):
        self.digest()
        return self.dequeue[-1]
        
    def pop(self):
        self.digest()
        return self.dequeue.pop()
        
    def put(self, value):
        self.enqueue.append(value)

    def digest(self):
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())
                
        
queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

