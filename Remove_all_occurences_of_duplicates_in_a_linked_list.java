class Solution {
    public Node removeAllDuplicates(Node head) {
        // code here
        Node temp=new Node(0);
        temp.next=head;
        Node prev=temp;
        while(head!=null){
            if(head.next!=null && head.data==head.next.data){
                while(head.next!=null && head.data==head.next.data){
                    head=head.next;
                }
                prev.next=head.next;
            }
            else{
                prev=prev.next;
            }
            head=head.next;
        }
        return temp.next;
    }
    
}
