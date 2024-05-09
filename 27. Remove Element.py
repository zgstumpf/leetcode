class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        w = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[w] = nums[i]
                w += 1

        return w
