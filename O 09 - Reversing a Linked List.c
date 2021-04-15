LinkedListNode* Reverse(LinkedListNode* head) {
LinkedListNode *prv,*cur,*fwd;
cur=head;
prv=NULL;
while(cur!=NULL){
fwd=cur->next;
cur->next=prv;
prv=cur;
cur=fwd;
}
head=prv;
return head;
}
