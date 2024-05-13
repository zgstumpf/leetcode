class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # first 2 nums will always be fine
        if len(nums) <= 2:
            return len(nums)

        # third num (index 2) might be bad, so get ready to overwrite it.
        w = 2  # w is write index

        # search for a suitable num 
        for s in range(2, len(nums)):  # s is search index

            # Example
            # 1, 1, 1, 2
            #       w  s 
            # w is third duplicate
            # moment we encounter third duplicate, goal is to search
            # for num to overwrite it
            if nums[s] != nums[w - 2]:
                nums[w] = nums[s]
                w += 1

        return w
