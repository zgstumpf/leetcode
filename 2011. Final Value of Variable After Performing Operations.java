class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int X = 0;
        for (String op : operations) {
            switch (op.charAt(1)) {
                case '+': X++; break;
                case '-': X--; break;
            }
        }
        return X;
    }
}
