class ListNode:
    """
    A node in a doubly linked list.
    """

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# remove /./ (dont remove first / if it is first in string)
# /../ -> remove itself and remove previous dir
#   Ex: A/B/../C -> A/C
# remove / if there is one at end (dont remove if it is also first)
# replace multiple /'s with single /


class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')

        # Remove '' from dirs
        dirs = [d for d in dirs if d]

        if dirs == []:
            return '/'

        head = ListNode(dirs[0])

        # Make linked list
        cur = head
        for i in range(1, len(dirs)):
            cur.next = ListNode(dirs[i])
            cur.next.prev = cur
            cur = cur.next

        # iterate through doubly linked list and apply rules

        # all '/' are removed with split('/')
        # path must start with '/'
        head.prev = ListNode('/', head)

        # keep track of root, we will need it later
        root = head.prev

        cur = head
        while cur:
            if cur.val == '.':
                # Fix next pointer
                #      cur
                # a -> .   -> c
                #   <-     <-
                cur.prev.next = cur.next
                # Result: a's next pointer points to c
                #      cur
                #   |---------v
                # a -  .   -> c
                #   <-     <-

                # c's previous pointer still points to '.'
                # Fix previous pointer
                if cur.next:  # if /./ is at end, do nothing
                    cur.next.prev = cur.prev
                # Result: c's previous pointer points to a
                # Note '.' is still there, just inaccessible
                #      cur
                #   |---------v
                # a -  .   -> c
                # ^ <-        |
                # |------------

            elif cur.val == '..':
                if cur.prev.prev:
                    # Fix next pointer
                    cur.prev.prev.next = cur.next

                    # Fix previous pointer
                    if cur.next:
                        cur.next.prev = cur.prev.prev
                else:
                    # Situation:
                    # / -> .. -> None

                    # Fix next pointer
                    cur.prev.next = cur.next

                    # Fix previous pointer
                    if cur.next:
                        cur.next.prev = cur.prev

            cur = cur.next

        ans = []
        cur = root
        while cur:
            # ignore root
            if cur.val != '/':
                ans.append(cur.val)
            cur = cur.next

        return "/" + "/".join(ans)
