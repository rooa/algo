class QueueByStack():
    def __init__(self):
        """
        initialize Queue with List(serving as a stack).
        """
        self.stack = []

    def empty(self):
        """
        Check whether a stack is empty
        """
        return len(self.stack) == 0
        

    def enqueue(self,x):
        self.stack.append(x)

    def dequeue(self):
        
        def recurse(stack):
            top = stack.pop()
            if len(stack) == 0:
                return top
            else:
                item = recurse(stack)
                stack.append(top)
                return item

        if self.empty():
            return None
            
        return recurse(self.stack)


    def __str__(self):
        return str(self.stack)

if __name__ == '__main__':

    s = QueueByStack()
    for i in range(1,5):
        s.enqueue(i**2)

    print "Initial: ", s
    s.dequeue()
    print "dequeued.."
    print "After 1: ", s
    s.dequeue()
    print "dequeued.."
    print "After 2: ", s

    
   
        
