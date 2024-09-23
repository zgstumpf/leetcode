class Solution {
    public boolean isPalindrome(String s) {
        // left pointer iterates left to right
        // right pointer iterates right to left
        // when moving pointers, skip spaces and punctuation - use Character.isLetterOrDigit(char c)
        // then compare chars after .toLowerCase()
        // if equal, move pointers again
        // if not equal, return false
        // stop loop when left >= right
        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            while (l < s.length() && !Character.isLetterOrDigit(s.charAt(l))) {
                l++;
            }
            while (r > 0 && !Character.isLetterOrDigit(s.charAt(r))) {
                r--;
            }
            if (!(l < r)) {
                break;
            }
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            } else {
                l++;
                r--;
            }
        }
        return true;
    }
}
