The number of applicants have now increased and the coach is now tired of trying to eliminate the shorter players. Instead, he just wants everyone to come and stand in ascending order of their heights, following the same routine he tried to use above.

Formally, use the selection sort technique to sort the array of player heights.

INPUT

The first line of input is n (1≤n≤100), the number of applicants for the basketball team The second line of input is the heights of the n players (positive numbers) each separated by a space.

OUTPUT

Print the heights of the players in a line after the sorting routine.

Sample Input 0

8
3 4 5 2 4 10 18 1
Sample Output 0

1 2 3 4 4 5 10 18

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int i,j,n,arr[100],t=0;
    cin>>n;
    for(i=0;i<n;i++)cin>>arr[i];
    for(i=0;i<n;i++)
    for(j=0;j<n-i-1;j++)
    {
        if(arr[j]>arr[j+1]){
        t=arr[j];
        arr[j]=arr[j+1];
        arr[j+1]=t;
        }
    }
    for(i=0;i<n;i++)cout<<arr[i]<<" ";
    return 0;
}
