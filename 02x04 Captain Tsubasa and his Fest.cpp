The very famous captain Oozora Tsubasa of football club Nankatsu FC decided to popularize football in Japan by organizing a football fest. The fest had many events for different sections of people.
For the awesome coders of CCC, there was an event called PASS and BACK.
In this event, the coders were given N passes and players having ids between 1 and 1000000.
Initially some player with a given id had the ball in his possession. The coders had to make a program to display the id of the player who possessed the ball after exactly N passes.

Description of the passes:
There were two kinds of passes:
1. P ID
2. B

Explanation :

For the first kind of pass, the player in possession of the ball passes the ball to player with id = ID while for the second kind of a pass, the player in possession of the ball passes the ball back to the player who had passed the ball to him.

NOTE:

It is guaranteed that the given order of all the passes will be a valid order .

Input Format

The first line of the input contains the number of test cases. For each test case, two space separated integers N and ID ( of the player possessing the ball in the very beginning).
N lines follow describing the passes. ( for description of the passes, refer the statement above. )

Constraints

1≤T≤100
1≤N≤100000
1≤ID≤1000000

Output Format

Output to each test case should be a single line containing the "Player" ID (quotes for clarity) of the player who possesses the ball after N passes.

Sample Input 0

1
10 23
P 86
P 63
P 60
B
P 47
B
P 99
P 9
B
B
Sample Output 0

Player 9
#include<iostream>
using namespace std;
 
int main()
{
     int T; cin>>T;
     while(T--)
     {
          int N; cin>>N;
          int curr; cin>>curr; 
          int prev,i; 
          for(i=1;i<=N;i++) { 
          char c; cin>>c; 
          if(c=='P') { 
               prev = curr;  
               cin>>curr;
          } 
          else { 
               int temp=curr; 
               curr = prev; 
               prev = temp;  
          } 
     } 
     cout<<"Player "<<curr<<endl;  
   } 
}
