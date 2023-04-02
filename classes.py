import heapq

# Class
class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)
    
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()

obj = MyClass([1,2,3])
print(obj.getDoubleLength())
