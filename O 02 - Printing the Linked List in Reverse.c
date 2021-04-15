void ReversePrint(LinkedListNode* head) {

if(head==NULL)return;

  if(head){

    ReversePrint(head->next);

    printf("%d ",head->val);

  }

}
