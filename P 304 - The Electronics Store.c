There is a queue of n people in front of the local electronics store. All of them have their phones at various battery percentages and are looking to buy a portable charger quickly before their battery runs out. The server at the counter understands this and he doesn’t want any of his customers’ phones to run out of charge. He, being an algorithmist, quickly determines that he wants to implement bubble sort technique to sort the customers in the queue, such that, the person whose phone is going to die the quickest, comes to the front of the line and gets a portable charger.

The server at the counter is an algorithmist and not a programmer, hence he asks you to do the job for him.

Formally, sort an array using bubblesort.

INPUT

The first line of input is n (1≤n≤100), the number of customers in the queue
The second line of input is the battery percentages of the n customers (positive numbers less than 100) each separated by a space.

OUTPUT

Print the battery percentages of the customers in a line after the sorting is completed.

Sample Input 0

8
3 4 5 2 4 10 18 1
Sample Output 0

1 2 3 4 4 5 10 18

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n,a[100],t,i,j;
    scanf("%d",&n);
    for(i=0;i<n;i++)scanf("%d",&a[i]);
    for(i=0;i<n;i++){
    for(j=0;j<n-i-1;j++){
    if(a[j]>a[j+1]){
    t=a[j];
    a[j]=a[j+1];
    a[j+1]=t;
    }
    }
    }
    for(i=0;i<n;i++)printf("%d ",a[i]);
    return 0;
}
