class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            newNum = 0
            for digit in str(num):
                newNum += int(digit)
            num = newNum
        return num
