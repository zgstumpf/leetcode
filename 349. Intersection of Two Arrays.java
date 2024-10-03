import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<>();
        // hash smaller array
        int[] arrayToBeHashed = nums1.length <= nums2.length ? nums1 : nums2;
        for (int num : arrayToBeHashed) {
            set.add(num);
        }

        int[] arrayToBeIterated = arrayToBeHashed == nums1 ? nums2 : nums1;
        Set<Integer> resultsSet = new HashSet<>();
        for (int num : arrayToBeIterated) {
            if (set.contains(num)) {
                resultsSet.add(num);
            }
        }

        int[] resultsArr = new int[resultsSet.size()];
        int index = 0;
        for (int num : resultsSet) {
            resultsArr[index] = num;
            index++;
        }

        return resultsArr;

    }
}
