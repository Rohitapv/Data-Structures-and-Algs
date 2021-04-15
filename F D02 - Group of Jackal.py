The function accepts a positive integer array ‘array’ of size ’n’ as its argument. Implement the function to find the Jackal elements in the array and return their sum.

An element is a Jackal in the array if it is STRICTLY greater than all the elements to its right side. the rightmost element is always a Jackal.

Input Format

Complete the given Function

Constraints

The answer would lie in Integer range.

Output Format

Return the sum of the Jackal elements of the array

Sample Input 0

5
5 4 3 2 1
Sample Output 0

15

#!/bin/python3

import sys

def LearderSum(arr,n):
    k=set()
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]<arr[j]):
                break
        if j==n-1:k.add(arr[i])
    print(sum(k))
if __name__ == "__main__":
    n = int(input().strip())
    array = list(map(int, input().strip().split(' ')))
    LearderSum(array,n)
