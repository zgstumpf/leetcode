class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # frequency method
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        zero = one = two = 0
        if 0 in counts:
            zero = counts[0]
        if 1 in counts:
            one = counts[1]
        if 2 in counts:
            two = counts[2]

        # [::] to modify nums in-place
        nums[::] = [0] * zero + [1] * one + [2] * two

        return nums
