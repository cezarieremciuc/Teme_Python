from Matrix import Matrix
from Stack import Stack
from Queue import Queue

if __name__ == "__main__":
# Matrix
    print("\nMatrix:")
    matrix1 = Matrix(3, 4)
    matrix2 = Matrix(3, 4)

    print(matrix1.__repr__())

    # set 
    matrix1[0,0] = 100
    print(matrix1.__repr__())

    # get
    val1 = matrix1[0,0]
    print(val1)

    # transposed
    print(matrix1.getTransposed())

    # multiplication
    print(matrix1 * matrix2)

    # addition
    print(matrix1 + matrix2)

    # map
    factor1 = 3
    print(matrix1.mapMatrix(lambda e: e * factor1))

# Stack
    print("\nStack:")
    stack1 = Stack()
    
    print(stack1.isEmpty())

    # push
    stack1.push(1)

    # peek
    print(stack1.peek())
    stack1.push(2)	
    stack1.push(3)

    # pop
    print(stack1.pop())
    print(stack1.pop())

    print(stack1.isEmpty())
    print(stack1.size())

# Queue
    print("\nQueue:")
    queue1 = Queue()

    # push
    queue1.push(1)
    queue1.push(2)

    # peek
    print(queue1.peek())
    queue1.push(3)

    # pop
    print(queue1.pop())
    print(queue1.pop())
    print(queue1.pop())

    queue1.push(5)
    print(queue1.peek())



