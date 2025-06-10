from collections import deque
class Queue:
    def __init__(self):
        self.q=deque()
    def enqueue(self,val):
        self.q.append(val)     #adding val to right
    def dequeue(self):
        if not self.is_empty():
            self.q.popleft()
        else:
            print("queue is underflow")
    def front(self):
        if not self.is_empty():
            print(self.q[0])
        else:
            print("queue empty")
    def is_empty(self):
        return len(self.q)==0
    def display(self):
        print("Queue: ",list(self.q))
obj=Queue()
obj.enqueue(4)
obj.enqueue(10)
obj.enqueue(32)
obj.dequeue()
obj.display()
obj.front()