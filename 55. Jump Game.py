class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Start at end and go backwards
        # If nums was A, B, C, ask:
        # Can I go to C from B? If yes, can I go to B from A?

        i = len(nums) - 2
        while i >= 0:
            jumpsNeeded = 1
            while nums[i] < jumpsNeeded:
                i -= 1
                if i < 0:
                    return False
                jumpsNeeded += 1
            i -= 1
        return True
