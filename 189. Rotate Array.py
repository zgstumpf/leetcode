class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rotated = [None] * len(nums)
        for idx, num in enumerate(nums):
            rotated[(k + idx) % len(nums)] = num
        nums[:] = rotated
