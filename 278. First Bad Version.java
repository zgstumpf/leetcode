/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        // This method uses binary search.

        int low = 1; // First version is 1, not 0.
        int mid;
        int high = n - 1; // We already know n is a bad version.

        // Not an endless loop because it breaks when the bad version
        // is returned, and there must be a bad version since n is bad.
        while (true) {

            // mid could be calculated with (high + low) / 2
            // But, if high and low are big enough, adding them
            // could exceed Java's Integer.MAX_VALUE and error.
            // This formula calculates mid without risking that error.
            mid = ((high - low) / 2) + low;
            // if high=low, mid=high (occurs if n is the first bad version)
 
            if (isBadVersion(mid)){
                if (!isBadVersion(mid - 1)) {return mid;}
                if (mid - 1 == 1) {return 1;} // first version is bad
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
    }
}
