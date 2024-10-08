class Solution {
    public String mergeAlternately(String word1, String word2) {
        char[] resultArr = new char[word1.length() + word2.length()];
        int resultArrIdx = 0;
        String shorterWord = (word1.length() < word2.length() ? word1 : word2);
        String longerWord = (shorterWord == word1 ? word2 : word1);
        int i = 0;
        for (; i < shorterWord.length(); i++) {
            resultArr[resultArrIdx] = word1.charAt(i);
            resultArrIdx++;
            resultArr[resultArrIdx] = word2.charAt(i);
            resultArrIdx++;
        }
        for (; i < longerWord.length(); i++) {
            resultArr[resultArrIdx] = longerWord.charAt(i);
            resultArrIdx++;
        }
        return new String(resultArr);
    }
}
