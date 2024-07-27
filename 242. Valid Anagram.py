class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # char: count
        sDict = {}
        for char in s:
            if char not in sDict:
                sDict[char] = 1
            else:
                sDict[char] += 1

        for char in t:
            if char not in sDict:
                return False
            else:
                if sDict[char] > 1:
                    sDict[char] -= 1
                else:
                    del sDict[char]

        return True
