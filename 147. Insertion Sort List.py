# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(float('-inf'), head) # dummy node to make things easier
        prev = dum.next # prev (previous) is the element before cur
        cur = prev.next # cur is the current element
        while cur:
            if cur.val < prev.val:
                # In a sorted list, the previous element should not be bigger.
                # So, cur goes somewhere before prev. To find exactly where,
                # starting at the beginning of the list, look for the first element greater
                # than cur, then put cur before this element.
                new = dum.next # new is the element that will eventually be greater than cur
                newprev = dum # newprev is new's previous element
                while new.val <= cur.val:
                    # move newprev and new forward
                    newprev = new
                    new = new.next
                # Found new element greater than cur. Reposition the elements.
                prev.next = cur.next # must do this first or some nodes may be orphaned
                newprev.next = cur
                cur.next = new
                # Move prev and cur to next numbers that need analyzing.
                # Prev already points to number that was bigger
                # than cur and was switched
                cur = prev.next
            else:
                # Move prev and cur forward.
                prev = cur
                cur = cur.next
        return dum.next
