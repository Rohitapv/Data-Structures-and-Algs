find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input Format

The first (and the only) input line contains integer number w — the weight of the watermelon bought by them.

Constraints

1 ≤ w ≤ 100

Output Format

Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Sample Input 0

8
Sample Output 0

YES
Explanation 0

The boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos)

n=int(input())
if(n==2):
    print("NO")
elif(n%2==0):
    print("YES")
else:
    print("NO")
