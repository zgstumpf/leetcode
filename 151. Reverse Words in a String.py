class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([char for char in s.split(' ') if char][::-1])
