class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # add dummy number at end to avoid errors with final num
        # by problem constraints, max num is 2**31 - 1,
        # adding 2 to this means when we come across it,
        # code will detect range ending
        nums.append(2**31 - 1 + 2)

        ranges = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i - 1]:
                if nums[i - 1] == start:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
        return ranges
