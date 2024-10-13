/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode cur = head;
        while (cur.next != null) {
            int gcd = gcd(cur.val, cur.next.val);
            ListNode newNode = new ListNode(gcd, cur.next);
            cur.next = newNode;

            cur = cur.next.next;
        }

        return head;
    }

    private int gcd(int a, int b) {
        int gcd = Math.min(a, b);
        while (gcd > 0){
            if (a % gcd == 0 && b % gcd == 0) {
                return gcd;
            }
            gcd--;
        }
        return -1;
    }
}
