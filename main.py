import collections
from datetime import datetime
import heapq
from io import StringIO

def main():
    # Variables
    print("*** Intro into variables ***")
    nickname = None
    a, b = "apple", "banana"    # multiple declarations
    a, b = b, a                 # swap without use of temp variable
    n = Node(5)
    n.next = Node(float("inf"))  # no max int

    def dfs(num):
        print("dfs(%d)" % num, end="...")  # no new line using custom end=
        if num == 0:
            print("Reached zero in dfs() call. Will return!")
            return True
        elif num < 0:
            print("Only values >=0 are allowed")
            return False
        return dfs(num - 1)

    dfs(3)

    print("\nnext up:")
    # One dimensional lists
    print("*** Lists demo ***")
    listOne = [0] * 2  # list of len=2, filled with zeros
    listTwo = [3, 1, 2]
    listTwo.append(4)
    listTwo.sort()             # asc
    listTwo.sort(reverse=True)  # desc
    # swap first and last (or any valid index)
    listTwo[0], listTwo[len(listTwo)-1] = listTwo[len(listTwo)-1], listTwo[0]

    for i in range(len(listOne)):  # range(len(listOne), -1, -1) is need to walk from end
        print("List One index: %d has value of %d" % (i, listOne[i]))

    for i, v in enumerate(listTwo):
        print("List Two index: %d has value of %d" % (i, v))

    for v in listTwo:
        pass

    listThree = listTwo
    listTwo[0] = 5
    print("Both lists change at the same time:", listThree, listTwo)

    destList = listTwo.copy()
    listTwo[0] = 7
    print("Copy helps isolate lists:", destList, listTwo)

    print("\nnext up:")
    print("*** Multidimensional lists demo ***")
    matrix = [[1, 2, 3], [4, 5, 6]]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print("%d is the value as row=%d and column=%d" %
                  (matrix[r][c], r, c))
    dp = [[[0]*4]*3]*2  # i,j,k
    print(dp)  # 2x3x4 matrix of zeros

    intervals = [[3, 5], [2, 6]]  # i[0] is start, i[1] is end
    # sorting by asc start here; add reverse=True for desc
    intervals.sort(key=lambda i: i[0])
    print(intervals)

    print("\nnext up:")
    # Maps
    print("*** Dictionary demo ***")
    mapOne = {}
    mapTwo = {"Alice": 3, "Bob": 5}
    for k, v in mapTwo.items():
        print("%s is %d" % (k, v))
    if "python" not in mapOne:
        mapOne["python"] = 1
    if "python" in mapOne:
        print("%s is found with value of %d" % ("python", mapOne["python"]))

    # with more complex keys:
    mapThree = {(1, 3): True}  # using tuple as key
    k = tuple([1, 3])
    if k in mapThree:
        print("Entry with complex key %s is present!" % str(k))
    del mapThree[k]
    # len(..) == 0 check is redundant, just demo
    if k not in mapThree and len(mapThree) == 0:
        print("Entry with complex key %s is gone!" % str(k))

    print("\nnext up:")
    print("*** Misc demo ***")

    def fn(req, opt=1, *args, **kwargs):
        print("Required param value is: ", req)
        print("Optional param value is: ", opt)
        print("Sum of arg values: ", sum(args))
        for k, v in kwargs.items():
            print("Param %s=%s" % (k, v))
        return " ✅ done"
    print("Call to custom variadic function:",
          fn(4, "opt ;)", 1, 2, 3, name="Python"))

    print("\nnext up:")
    print("*** List used as a queue and stack ***")

    queue = collections.deque()  # can also use simple list [], deque is more efficient
    queue.append(1)         # add element to a queue
    queue.extend([5, 6, 7, 8])  # add multiple elements (from another list
    queue.insert(0, 42)     # push value (i.e. 42) to front
    while len(queue) > 0:
        print("%d..." % queue.popleft(), end="")
        # Possible to use slicing or queue.pop(0) if queue defined as list
        # next = queue[0]; queue = queue[1:]
        # You pop multiple elements, and re-slice once. Can be used in BFS traversal.
        # queue[3:] means indexes 3,4,5,6...up to len(queue), i.e. queue[3:len(queue)]

    print("queue is now empty")

    stack = collections.deque()  # can also use simple list [], deque is more efficient
    stack.append(1)             # add element to a stack
    stack.extend([5, 6, 7, 8])     # add multiple elements (from another list)
    while len(stack) > 0:
        # variation on use of end= (see above queue print)
        print(stack.pop(), end="...")
        # Note: stack.pop() is same for either list [] or deque()
        # Slicing is possible, but creates a copy of the list, better use pop()
        # stack = stack[:len(stack)-1] # last element index in slicing is non-inclusive
        # slice[1:5] means indexes 1,2,3,4
        # slice[:5] means indexes 0,1,2,3,4

    print("stack is now empty")

    print("\nnext up:")
    print("*** Strings demo ***")
    s = "Hello, 世界"
    for c in s:
        if not((c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z') or ord(c) <= 255):
            print("Non-ascii char:", c)
    for b in bytes(s, "UTF-8"):
        print(b)

    i = 0
    for word in s.split(","):
        i += 1
        print("Word #%d: %s" % (i, word.strip()))

    print("Checking contains with .. in s =>", "llo" in s)     # True
    print("Checking s.startswith() =>", s.startswith("Hello"))  # True
    print("Checking s.endswith() =>", s.endswith("界"))        # True
    print("Checking sep.join([words]) =>", " ".join(["Hello", "World"]))

    sb = StringIO()  # closest alternative to a string builder
    sb.write("Building formatted string")
    sb.write(" with some numbers: %6.2f" % 12.5)
    sb.write(" and date: ")
    sb.write(datetime.now().strftime("%a %b %d"))

    print(sb.getvalue())
    # Alternatively can just join strings:
    print("".join(
        ["Building formatted string by joining list of strings",
         " with some numbers: %6.2f" % 12.5,
         " and date: ",
         datetime.now().strftime("%a %b %d")])
    )

    print("\nnext up:")
    print("*** Heap demo ***")

    minHeap, maxHeap = [], []
    # if list if not empty, heapify it (not needed for empty list)
    heapq.heapify(minHeap)
    for i in range(1, 5, 1):  # 1..4
        heapq.heappush(minHeap, i)
        # for max heap just change the sign of values when push and pop
        heapq.heappush(maxHeap, -i)

    print("Max in max heap: ", -1*maxHeap[0])
    print("Min in min heap:", minHeap[0])
    while maxHeap:  # can also go with `len(maxHeap) > 0`
        print("Min: %d and max: %d" %
              (heapq.heappop(minHeap), -1*heapq.heappop(maxHeap)))


class Node:
    def __init__(self, v):
        self.val = v
        self.next = None


if __name__ == "__main__":
    main()
