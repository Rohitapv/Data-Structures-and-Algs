You are given an array of N integers A1, A2, A3... AN.
Your task is to write a program to print the maximum value f(i, j) for all 1 <= i,j <= N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes the absolute value of x.
Input Format
First line contains N, the size of the array.
Second line contains N space separated integers, the elements of the array.
Constraints
1 <= N <= 106
1 <= Ai <= 106
Output Format
Output one integer, the maximum possible value of function f(i, j).
Sample Input 0
3
1 3 -1
Sample Output 0
5
  
#O(n^2)
"""n=int(input())
l=list(map(int,input().split()))
res=0
for i in range(n):
    for j in range(i,n):
        val = abs(l[i]-l[j])+abs(i-j)
        if val > res:
            res = val

print(res)"""
#O(n)
def maxDistance(array):
    max1 = -2147483648
    min1 = +2147483647
    max2 = -2147483648
    min2 = +2147483647

    for i in range(len(array)):
        max1 = max(max1, array[i] + i)
        min1 = min(min1, array[i] + i)
        max2 = max(max2, array[i] - i)
        min2 = min(min2, array[i] - i)
    return max(max1 - min1, max2 - min2)
n=int(input())
array = list(map(int,input().split()))

print(maxDistance(array))
