""" 
Python implementation of stack is just basically its
list itself
"""


if __name__ == "__main__":
    stack = [1,2,3,4,5,6]

    stack.append(7) #add item at the top of the stack 
    print("current stack after appended", stack)

    itemPopped = stack.pop() # pop the item at the top of the stack
    # in this case 7

    print("item popped is: ",itemPopped)
    print("current stack after pop", stack)
