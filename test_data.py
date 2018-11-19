from Classes import Testcase


tc1 = Testcase()
tc1.id = "1"
tc1.input = '23\n34'
tc1.timeout = 1

tc2 = Testcase()
tc2.id = "2"
tc2.input = """21\n34"""
tc2.timeout = 1


source_code_add_two_numbers = """
number1 = input()
number2 = input()

sum = int(number1) + int(number2)
print(sum)
"""

source_code_infinte_loop = """
while(True):
    print(1)
"""

tc3 = Testcase()
tc3.id = "3"
tc3.input = """1\n10\n12\n101\n101\n12"""
tc3.timeout = 1


source_binary_search_with_error = """
arr = []
for i in range(5):
    arr.append(input())

x = input()

def binarySearch (arr, l, r, x):

    if r >= l:

        mid = l + (r - l)/2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        return -1

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")
"""

source_binary_search = """

arr = []
for i in range(5):
    arr.append(input())

x = input()

def binarySearch (arr, l, r, x):

    if r >= l:

        mid = l + (r - l)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        return -1

result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")
"""
