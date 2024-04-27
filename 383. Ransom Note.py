class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Build ransomDict
        # Ex: 'aabccc' -> {'a': 2, 'b': 1, 'c': 3}
        ransomDict = {}
        for char in ransomNote:
            if char in ransomDict:
                ransomDict[char] += 1
            else:
                ransomDict[char] = 1
        
        # As we find chars we need, remove them from ransomDict
        for char in magazine:
            if char in ransomDict:
                ransomDict[char] -= 1
                if ransomDict[char] == 0:
                    del ransomDict[char]
        
        if len(ransomDict) == 0:
            return True

        # ransomDict still has some chars we couldn't fulfill
        return False
