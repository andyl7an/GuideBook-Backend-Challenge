'''
Back-End Challenge: "Shifted List Search"
Author: Andy Tan

Notes:
1. Function accepts a sorted (optionally rotated) list of integers as argument
2. The output is a single integer

'''


def search(input):
    left = 0
    right = len(input) - 1
    result = input[left]
    #check if array is rotated
    if (len(input) == 1 or input[left] < input[right]):
        return input[right]
    while (left <= right):
        #same as (right - left) /2, rewritten to prevent overflow and converted to integer
        mid = int((right - left)/2 + left)
        #left side is sorted, search right side
        if(input[left] <= input[mid]):
            left = mid 
        #right side is sorted, search left side
        else:
            right = mid - 1
        #if the result is the same as previous iteration, ans is found
        if(input[mid] == result):
            break
        result = input[mid]
    return result


def main():
    #some test cases following parameters of the challenge
    test1 = [8,9,10,11,1,3,7]
    test2 = [6,8,10,2,4]
    test3 = [2,4,6,8,10]
    test4 = [10,1,2,3,4,5]
    test5 = [6,10,1,2,3,4,5]
    test6 = [2,3,4,5,6,7,8,9,10,1]
    test7 = [10,10,1,2,3,4,5,5,6,6]
    out = search(test1)
    assert(11 == out)
    out = search(test2)
    assert(10 == out)
    out = search(test3)
    assert(10 == out)
    out = search(test4)
    assert(10 == out)
    out = search(test5)
    assert(10 == out)
    out = search(test6)
    assert(10 == out)
    out = search(test7)
    assert(10 == out)

if __name__ == "__main__":
    main()
