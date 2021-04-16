You are given an array A of size N.
You are also givena number K.
Let us define what K-Divisibility of an array means :
       K-Divisibility of an array is the number of unordered pairs (i,j) such that Ai + Aj is divisible by K.

Your task is to find and print the K-Divisibility of the given array A.
INPUT
First line contains two integers, size of array N and the value K.
Second line contains N space separated integers, ith of which denotes Ai.

OUTPUT
Print one value, the K-Divisibility of the array.
Sample Input 0
6 5
1 2 3 4 5 6
Sample Output 0
3

def countKdivPairs(A, n, K):
    
    # Create a frequency array to count
    # occurrences of all remainders when
    # divided by K
    freq = [0 for i in range(K)]

    # To store count of pairs.
    ans = 0

    # Traverse the array, compute the remainder
    # and add k-remainder value hash count to ans
    for i in range(n):
        rem = A[i] % K
        
        # Count number of ( A[i], (K - rem)%K ) pairs
        ans += freq[(K - rem) % K]
        
        # Increment count of remainder in hash map
        freq[rem] += 1

    return ans

# Driver code
if __name__ == '__main__':
    n,K=map(int,input().split())
    A = list(map(int,input().split()))
    print(countKdivPairs(A, n, K))

# This code is contributed by
# Surendra_Gangwar, Yadvendra Naveen
