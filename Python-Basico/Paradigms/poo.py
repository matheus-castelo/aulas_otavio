# Class

class MyClass:
    # Constructor
    def __init__(self, nums):  # SELF is just like THIS keywords, And in this case, the constructor are taking
        # a list of numbers.
        # Creating a Member Variables
        self.nums = nums
        self.size = len(nums)
    
    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()


# Creating a Object and Testing Methods
myObj = MyClass([1, 2, 3])
print(myObj.getLength())
print(myObj.getDoubleLength())


