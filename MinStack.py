"""
MinStack.py
            
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
        
Implement the MinStack class:
            
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""



class MinStack(object):
    """Going to use Python's built in array rather than implementing a linked list'"""

    def __init__(self):
        self.stack = []
        self.minimums = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        # add value
        self.stack.append(val)
        
        # update the minimums stack
        min_val = min(val, self.minimums[-1] if self.minimums else val)
        self.minimums.append(min_val)


    def pop(self):
        """
        :rtype: None
        """
        
        # return if no stack
        if len(self.stack) == 0:
            return None
            
        
        # remove last values
        self.stack.pop()
        self.minimums.pop()
        
        
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
            
        return self.stack[-1]

        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minimums) == 0:
            return None
            
        return self.minimums[-1]
        

# Your MinStack object will be instantiated and called as such:
obj = MinStack()

obj.push(-2)

obj.push(0)

obj.push(-3)

print(obj.getMin())
obj.pop()

print(obj.top())
print(obj.getMin())