class Solution {
    public void reverseString(char[] s) {
        int l = 0; // left pointer
        int r = s.length - 1; // right pointer
        while (l < r) {
            // swap
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;

            // move pointers
            l++;
            r--;
        }
    }
}
