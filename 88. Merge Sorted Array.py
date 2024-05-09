class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # last num in nums1 (not including placeholder 0's)
        j = len(nums2) - 1 # last num in nums2

        w = len(nums1) - 1 # write index

        # starting from end of each array, 
        # put bigger num at write index
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1

            w -= 1
        
