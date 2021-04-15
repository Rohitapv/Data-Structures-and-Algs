For example 100, 1000, 10000 are Barua Numbers whereas 101, 502, 625 are not Barua Numbers. Unfortunately one decimal number has crept into a list of Barua Numbers and Barua OS cannot find its product. Can you?

Input Format:

First line contains an integer N, total number of elements in the list.

Next N lines contains a number a[i] <= 10^18.

NOTE :
Out of the N numbers, there will be at most 1 decimal number and the remaining numbers will be Barua Numbers.
There may be no decimal numbers at all.

Output Format:
Print one number, the product of all the numbers.

Input Constraints:

1 <= N <= 10^6

1 <= A[i] <= 10^18

Sample Input 0

4
100
121
10
100
Sample Output 0

12100000

  
n=int(input())
s=0
p=1
for i in range(n):
    a=(int(input())) 
    while(a%10==0):
        s+=1
        a//=10
    p*=a
print(str(p)+"0"*s)
