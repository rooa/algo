"""
Queue implemented by LinkedList.
enqueue
dequeue
isEmpty
rotate

Also has
Deque & queue(Using ring buffer)

"""


class Queue:
    class Cell:
        def __init__(self, x, y = None):
            self.data = x
            self.next = y
    
    def __init__(self):
        self.rear = None
        self.size = 0

    def enqueue(self, x):
        if self.size == 0:
            self.rear = Queue.Cell(x)
            self.rear.next = self.rear
        else:
            new_cell = Queue.Cell(x, self.rear.next)
            self.rear.next = new_cell
            self.rear = new_cell
        self.size += 1
        
    def dequeue(self):
        if self.size == 0:
            raise IndexError
        front = self.rear.next
        self.rear.next = front.next
        self.size -= 1
        # The program above does nothing in case self.size == 1
        if self.size == 0:              
            self.rear = None

        return front.data
        
            
    def isEmpty(self):
        if self.size == 0: return True
        else: return False

    def peek(self):
        return self.rear.next.data

    def rotate(self, n = 1):
        if self.size == 0 or n < 1:
            raise IndexError
        while n > 0:
            self.rear =  self.rear.next
            n -= 1


class Deque():

    class Cell2():
        def __init__(self, x,y = None, z = None):
            self.data = x
            self.next = y
            self.prev = z

    def __init__(self):
        head = Deque.Cell2(None)
        head.next = None
        head.prev = None
        self.size = 0
        self.head = head

        
    def push_front(self,x):
        new_cell = Deque.Cell2(x,self.head.next,self.head)
        self.head.next.prev = new_cell
        self.head.next = new_cell
        self.size += 1
        # These flows fits even when there is only a header cell.

    def push_back(self,x):
        h = self.head
        p = h.prev
        new_cell = Deque.Cell2(x,h,p)
        h.prev = new_cell
        p.next = new_cell
        self.size += 1

    def pop_front(self):
        if self.size == 0: raise IndexError
        h = self.head
        q = h.next
        p = q.next
        h.next = p
        p.prev = h
        self.size -= 1
        return q.data
            
    def pop_back(self):
        if self.size == 0: raise IndexError
        h = self.head
        q = h.prev
        p = q.prev
        h.prev = p
        p.next = h
        self.size -= 1
        return q.data

    def peek_front(self):
        if self.size == 0: raise IndexError
        h = self.head
        return h.next.data
        
    def peek_back(self):
        if self.size == 0: raise IndexError
        h = self.head
        return h.prev.data
        
    def isEmpty(self):
        if self.size == 0:
            return True
        return False


class Queue_ring:
    def __init__(self, n=16):
        self.size = n
        self.front = 0
        self.rear = 0
        self.buff = [None] * n
        self.count = 0                  # number of data, which realizes isFull()

    def enqueue(self,x):
        if self.count == self.size: raise IndexError
        self.buff[self.rear] = x
        self.rear += 1
        if self.rear == self.size:self.rear = 0
        self.count += 1
        
    def dequeue(self):
        if self.count == 0: raise IndexError
        a = self.buff[self.front]
        self.front += 1
        if self.front == self.size: self.front = 0
        self.count -= 1
        return a
            
    def peek(self):
        if self.count == 0: raise NoItemError
        return self.buff[self.front]

    def isEmpty(self):
        if self.count == 0: return True
        return False

    def isFull(self):
        if self.count == self.size: return True
        return False

