// Runtime 1 ms
// Acceptance rate 28.9%
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        // iterate through array
        // when you come across 0, check neighbors to see if you can plant there
        // if you can, plant. change 0 -> 1.
        // if you can't, keep iterating until you can or you reach end of array
        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0
                && (i == 0                    || flowerbed[i - 1] == 0)
                && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)
               ) 
            {
                flowerbed[i] = 1;
                n--;
            }
        }
        return n <= 0;
    }
}
