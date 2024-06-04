# Variables are dynamically typed
n = 0
print("n =", n)  # n = 0
print()

n = "abc"
print("n =", n)  # n = abc

# Multiple assignments
a, b = 0, "hi"
i, j, k = 0.125, "hello", False
print("a =", a)  # a = 0
print("b =", b)  # b = hi
print()
print("i =", i)  # i = 0.125
print("j =", j)  # j = hello
print("k =", k)  # k = False

# Increment
a = a + 1  # good
a += 1  # good
# a++  # bad

# None is null (absence of value)
n = 4
print("n =", n)  # n = 4
n = None
print("n =", n)  # n = None

# If statements don't need parentheses
# or curly braces
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2
print()

# Parentheses needed for multi-line conditions
# and = &&
# or = ||
n, m = 1, 2
if (n > 2 and n != m) or n == m:
    n += 1
print()

# While loops are similar
n = 0
while n < 5:  # 0 1 2 3 4
    print(n)
    n += 1
print()

# Looping from i = 0 to i = 4
for i in range(5):  # 0 1 2 3 4
    print(i)
print()

# Looping from i = 2 to i = 5
for i in range(2, 6):  # 2 3 4 5
    print(i)
print()

# Loopong from i = 5 to i = 2
for i in range(5, 1, -1):  # 5 4 3 2
    print(i)
print()

# Division is decimal by default
print(5 / 2)  # 2.5

# Double slash rounds down (integer division)
print(5 // 2)  # 2

# CAREFUL: most languages round towards 0 by default
# so negative numbers will round down
print(-3 // 2)  # -2

# A workaround for rounding towards zero is to use
# decimal division and then convert to int
print(int(-3 / 2))  # -1
print()

# Modding is similar to most languages
print(10 % 3)  # 1
x, y = divmod(10, 3)
print("x =", x)  # x = 3
print("y =", y)  # y = 1
print()

# Except for negative values
print(-10 % 3)  # 2

# To be consistent with other languages modulo
import math

print(int(math.fmod(-10, 3)))  # -1
print()

# More math helpers
print(math.floor(3 / 2))  # 1 - round down
print(math.ceil(3 / 2))  # 2 - round up
print(math.sqrt(2))  # 1.4142135623730951 - square root
print(math.pow(2, 3))  # 8.0 - power
print()

# Max / Min Int
print(float("inf"))  # inf
print(float("-inf"))  # -inf

# Python numbers are infinite so they never overflow
print(math.pow(2, 200))  # 1.6069380442589903e+60

# But still less than infinity
print(math.pow(2, 200) < float("inf"))  # True
print()

# Arrays (called lists in Python)
arr = [1, 2, 3]
print(arr)  # [1, 2, 3]

# In Python, arrays are dynamic arrays by default
# Can be used as a stack
# Can push to array aka append
arr.append(4)  # O(1) - [1, 2, 3, 4]
arr.append(5)  # O(1) - [1, 2, 3, 4, 5]
print(arr)  # [1, 2, 3, 4, 5]

# Can pop from array
arr.pop()  # O(1) - delete and return the last item 5
print(arr)  # [1, 2, 3, 4]

# Technically it is an array not a stack, so
# we can insert into the middle
arr.insert(1, 7)  # O(n)
print(arr)  # [1, 7, 2, 3, 4]

# Index of access a value: 0(n)
arr[0] = 0  # item at index 0 becomes 0
arr[3] = 0  # item at index 3 becomes 0
print(arr)  # [0, 7, 3, 0, 4]
print()

# Intialize an array arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)  # [1, 1, 1, 1, 1]
print(len(arr))  # 5
print()

# CAREFUL: -1 is not out fo bounds,
# it's the last value
arr = [1, 2, 3, 4, 5, 6, 7]
print(arr[-1])  # 7

# Indexing -2 is the second to last value, etc.
print(arr[-2])  # 6
print()

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])  # [2, 3]

# Similar to for-loop ranges
# last index is non-inclusive
print(arr[0:4])  # [1, 2, 3, 4]
print()

# Unpacking
# CAREFUL: the number of variables on the left side
# should match the number of items into the array
a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3

# Loop through arrays
nums = [i for i in range(5)]
print(nums)  # [0, 1, 2, 3, 4]

# Loop using index
for i in range(len(nums)):  # 0 1 2 3 4
    print(nums[i])

# Loop without index
for num in nums:  # 0 1 2 3 4
    print(num)

# Loop with index and value
# enumerate function unpack the array
# each item with its corresponding index
for i, num in enumerate(nums):  # 0 0  1 1  2 2  3 3  4 4
    print(i, num)
print()

# Loop through multiple arrays simultaneously
# with unpacking
# zip functions take these 2 arrays
# and combine them into an array of pairs
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):  # 1 2  3 4  5 6
    print(n1, n2)
print()

# Reverse
nums = [1, 3, 5]
print(nums)  # [1, 3, 5]
# print(nums[::-1])  # create a new reserved array [5, 3, 1]
nums.reverse()  # reverse in-place
print(nums)  # [5, 3, 1]
print()

# Sorting
arr1 = [5, 4, 7, 3, 8]
print(arr1)
# arr1.sort()  # ascending order [3, 4, 5, 7, 8]
arr1.sort(reverse=True)  # descending order [8, 7, 5, 4, 3]
print(arr1)  # [8, 7, 5, 4, 3]
print()

# We can also sort a list of strings
# based on alphabetical order
arr2 = ["bob", "alice", "jane", "doe"]
print(arr2)  # ['bob', 'alice', 'jane', 'doe]
# arr2.sort()  # ascending order ['alice', 'bob', 'doe', 'jane']
# arr2.sort(reverse=True)  # descending order ['jane', 'doe', 'bob', 'alice']
print(arr2)

# Custom sort (by lenght of string)
arr2.sort(key=lambda x: len(x))
print(arr2)  # ['bob', 'doe', 'jane', 'alice']
print()

# List comprehension
mylist = [i for i in range(5)]
print(mylist)  # [0, 1, 2, 3, 4]

# 2D lists
# list of lists
# each row (inner list) is unique
my2d = [[0] * 4 for _ in range(4)]
print(my2d)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print()

# This won't work
# Because here we don't create unique rows (inner lists)
ll = [[0] * 4] * 4
print(ll)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print()

# Strings are similar to arrays
s = "abc"
print(s)
print(s[0:2])  # abc

# But they are immutable
# so, we can't modify them
# s[0] = 'A'  # we can modity the string `s`

# We can update O(n) time operation
s += "def"  # `s` becomes 'abcdef'
print(s)  # abcdef

# Valid numeric string can be converted
print(int("123") + int("123"))  # 246

# And numbers can be converted to strings
print(str(123) + str(123))  # 123123
print()

# In rare cases you may need the ASCII value
# of a character
print(ord("a"))  # 97
print(ord("b"))  # 98
print()

# Combine a list of strings
# (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))  # abcdef
print(" ".join(strings))  # ab cd ef
print("-".join(strings))  # ab-cd-ef

# Queues (double ended queue)
from collections import deque

queue = deque()
print(queue)
queue.append(1)
queue.append(2)  # O(1)
queue.append(3)
print(queue)  # deque([1, 2, 3])

queue.popleft()  # O(1) - delete and return the first item to the left 1
print(queue)  # deque([2, 3])

queue.appendleft(4)  # O(1) - append 4 to the left
print(queue)  # deque([4, 2, 3])

queue.pop()  # delete and return the last item to the right 3
print(queue)  # deque([4, 2])
print()

# Hashset
# Search O(1)
# Insert O(1)
# Remove O(1)
# Can't contain any duplicates
myset = set()

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)  # {1, 2, 3}
print(len(myset))  # 3
print(1 in myset)  # True
print(5 in myset)  # False
print()
myset.remove(1)  # delete 1 from myset
print(1 in myset)  # False
print(len(myset))  # 2
print(myset)  # {2, 3}
print()

# list to set
print(set([1, 2, 3]))  # {1, 2, 3}

# Sets comprehension
ss = {i for i in range(5)}
print(ss)  # {0, 1, 2, 3, 4}
print()

# Hashmap (aka dict)
mymap = {}
print(mymap)
mymap["john"] = 12
mymap[2] = "hi"
print(mymap)  # { 'john': 12, 2: 'hi' }
print(len(mymap))  # 2 - the number of keys

mymap["john"] = "doe"  # modify
print(mymap)  # { 'doe': 12, 2: 'hi' }
print("zuck" in mymap)  # False - check if a key is in Hashmap
mymap.pop(2)  # remove the key 2 and its value, and return the value ('hi')
print(mymap)  # { 'john': 'doe' }
print()

# Dicts comprehension
mm = {i: 2 * i for i in range(5)}
print(mm)  # { 0: 0, 1: 2, 2: 4, 3: 6, 4: 8 }

# Looping through maps
m = {"alice": 90, "bob": 70}
# Iterate through list of keys
for key in m:
    print(key, m[key])  # alice 90  bob 70

# Iterate through list of values
for val in m.values():
    print(val)  # 90 70

# Unpacking
for key, val in m.items():
    print(key, val)  # alice 90  bob 70
print()

# Use of the `get` method
li = ["a", "b", "c", "a", "d", "e", "b", "a"]
di = {}
print(li)  # ["a", "b", "c", "a", "d", "e", "b", "a"]
print(di)  # {}

for el in li:
    di[el] = di.get(el, 0) + 1

print(di)  # { "a": 3, "b": 2, "c": 1, "d": 1, "e": 1 }

print(di.get("a"))  # 3
print(di.get("d"))  # 1
print(di.get("z"))  # returns None if the key doesn't exist instead of raising an error
print()

# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)  # (1, 2, 3)

# Can index tuples
print(tup[0])  # 1
print(tup[1])  # 2
print(tup[2])  # 3
print()

# Can't modify tuples
# tup[0] = 5  # impossible to do this for example

# Can be used as key for hash map/set
m1 = {(1, 2): 3}
print(m1[(1, 2)])  # 3

ms = set()
ms.add((1, 2))
print(ms)  # ((1, 2))
print((1, 2) in ms)  # True
print()

# Lists can't be keys
# mm [[3, 4]] = 5

# Heaps
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])  # 2

# To loop through heap
while len(minHeap):
    print(heapq.heappop(minHeap))  # print and delete 2 3 4
print()

# No max heaps by default, work around is
# to use min heap and multiply by -1 when
# push & pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Here, Max is always at index 0
print(-1 * maxHeap[0])  # 4

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))  # print and delete 4 3 2
print()

# Build heap from initial values
a = [2, 1, 8, 4, 5]
print(a)  # [2, 1, 8, 4, 5]
print(a[0])  # 2
print()
heapq.heapify(a)  # a becomes a heap now
while a:
    print(heapq.heappop(a))  # print and delete 1 2 4 5 8
print()


# Functions
def myFunc(n, m):
    return n * m


print(myFunc(3, 4))  # 12
print()


# Nested functiona have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c

    return inner()


print(outer("a", "b"))  # abc
print()


# Can modify objects but not reassign
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *= 2

    helper()
    print(arr, val)


nums = [1, 2]
val = 3
double(nums, val)  # [2, 4] 6


# Class
class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)

    # self keyword required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()
