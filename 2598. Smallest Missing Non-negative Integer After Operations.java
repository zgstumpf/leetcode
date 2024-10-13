import java.util.Map;
import java.util.HashMap;

class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        // Can include any positive integers >= 0
        // If a starting point is used to satisfy a value for MEX, that specific
        // starting point can't be used again.
        // But the value of the starting point can be used again.
        // nums            = 0, 5   value = 5
        // starting points = 0, 0
        // {0=2} means I can start at 0, only 2 times.
        Map<Integer, Integer> startingPointsAndCounts = new HashMap<>();

        for (int num : nums) {
            int remainder = num % value;
            if (remainder < 0) {
                remainder += value;
            }
            if (startingPointsAndCounts.containsKey(remainder)) {
                startingPointsAndCounts.put(remainder, startingPointsAndCounts.get(remainder) + 1);
            } else {
                startingPointsAndCounts.put(remainder, 1);
            }
        }

        int MEX = 0;
        int modToFind = MEX % value;
        while (startingPointsAndCounts.containsKey(modToFind) &&
                (startingPointsAndCounts.get(modToFind) >= 1)) {
            startingPointsAndCounts.put(modToFind, startingPointsAndCounts.get(modToFind) - 1);
            MEX++;
            modToFind = MEX % value;
        }
        return MEX;
    }
}
