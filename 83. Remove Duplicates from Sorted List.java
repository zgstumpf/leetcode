/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    // Runtime 0 ms
    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head; // cur: current node
        while (cur != null && cur.next != null) {
            while (cur.next != null && cur.val == cur.next.val) {
                // cur and cur.next are duplicates,
                // so redirect cur.next to node after cur.next
                cur.next = cur.next.next;
            }
            cur = cur.next;
        }
        return head;
    }
}
