#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d",&n);
    int arr[n],i;
    for(i=n-1;i>=0;i--){
    scanf("%d",&arr[i]);
    }
    for(i=0;i<n-1;i++)
    printf("%d->",arr[i]);
    printf("%d",arr[n-1]);
    return 0;
}
