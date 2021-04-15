You are given an array of N integers which is a permutation of the first N natural numbers. You can swap any two elements of the array. You can make at most K swaps. What is the largest permutation, in numerical order, you can make?

Input Format

The first line of the input contains two integers, N and K, the size of the input array and the maximum swaps you can make, respectively. The second line of the input contains a permutation of the first N natural numbers.

Constraints

1≤N≤10^5 1≤K≤10^9

Output Format

Print the lexicographically largest permutation you can make with at most K swaps

Sample Input 0

5 1
4 2 3 5 1
Sample Output 0

5 2 3 4 1
#swapping 1st element with min element in rest of ele k times
def Kswap(arr,n,k):
    pos={}
    for i in range(n):
        pos[arr[i]]=i
    for i in range(n):
        if k==0:break
        if arr[i]==n-i:continue
        temp=pos[n-i]
        pos[arr[i]]=pos[n-i]
        pos[n-i]=i
        arr[temp],arr[i]=arr[i],arr[temp]
        k=k-1
n,k=map(int,input().split())
arr=list(map(int,input().split()))
Kswap(arr,n,k)
print(" ".join(map(str,arr)))
