class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0 # write index
        prev = -999 # previous unique num (placeholder for now)

        for i in range(len(nums)):
            if nums[i] != prev:
                nums[w] = nums[i]
                w += 1
                prev = nums[i]
        
        return w
