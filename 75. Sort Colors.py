class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = white = blue = 0

        for num in nums:
            match num:
                case 0:
                    red += 1
                case 1:
                    white += 1
                case 2:
                    blue += 1

        # [::] to modify nums in-place - Space O(1)
        nums[::] = ([0] * red) + ([1] * white) + ([2] * blue)

        return nums
