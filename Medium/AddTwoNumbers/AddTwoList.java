package Medium.AddTwoNumbers;


public class AddTwoList {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int sum=0;
        int car=0;
        ListNode first = null;
        ListNode last = null;
        while(l1 != null || l2 != null || car > 0){
            if(l1 != null && l2!= null){
                sum = l1.val + l2.val + car;
                l1 = l1.next;
                l2 = l2.next;
            } else if(l1 !=null){
                sum = l1.val +  car;
                l1 = l1.next;
            } else if(l2 != null){
                sum = l2.val +  car;
                l2 = l2.next;
            } else{
                sum = car;
            }
            car = sum >= 10 ? sum/10 : 0;
            sum = car > 0 ? sum%10 : sum;
            if(first == null){
                first = new ListNode(sum);
                last = first;
            }else{
                last.next = new ListNode(sum);
                last = last.next;
            }
        }
        return first;
    }
}

 class ListNode {
    int val;
    ListNode next;
    ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
