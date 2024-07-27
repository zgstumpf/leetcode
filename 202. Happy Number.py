class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        while n != 1:
            n = sum([int(digit) ** 2 for digit in str(n)])
            if n in results:
                return False
            results.add(n)
        return True
