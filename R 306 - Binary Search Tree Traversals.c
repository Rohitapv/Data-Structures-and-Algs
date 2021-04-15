Print the resultant binary search tree's pre-order, in-order and post-order traversal on three different lines.
Input Format
First line contains a number N. Next line contains N integers.
Constraints
1 <= N <= 1000
Output Format
Output 3 lines. First line denoting the preorder traversal, second line denoting the inorder traversal and the last line denoting the postorder traversal.
Sample Input 0
10
12 3 5 11 15 5 4 4 8 15 
Sample Output 0
12 3 5 5 4 4 11 8 15 15 
3 4 4 5 5 8 11 12 15 15 
4 4 5 8 11 5 3 15 15 12 
  
  #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define scan(x) scanf(" %d", &x)
struct TreeNode {
    int x;
    struct TreeNode* L;
    struct TreeNode* R;
};
typedef struct TreeNode TreeNode;
TreeNode* newNode(int _x) {
    TreeNode* node = (TreeNode*) malloc(sizeof(TreeNode));
    node->x = _x;
    node->L = node->R = NULL;
  return node;
}
TreeNode* insert(TreeNode* node, int val) {
    if (node == NULL) return newNode(val);
    if (val <= node->x) node->L = insert(node->L, val);
    else node->R = insert(node->R, val);
return node;
}

/*********************************************************/

void preorder(TreeNode* Root)
{
if(Root){
printf("%d ",Root->x);
preorder(Root->L);
preorder(Root->R);
}
}
void inorder(TreeNode* Root)
{
if(Root){
inorder(Root->L);
printf("%d ",Root->x);
inorder(Root->R);
}
}
void postorder(TreeNode* Root)
{
if(Root){
postorder(Root->L);
postorder(Root->R);
printf("%d ",Root->x);
}
}

/*******************************************************/

int main() {
    int val, N; scan(N);
    TreeNode* Root = NULL;
    for (int i = 1; i <= N; i++) {
        scan(val);
        Root = insert(Root, val);
    }
    preorder(Root);
    printf("\n");
    inorder(Root);
    printf("\n");
    postorder(Root);
}
