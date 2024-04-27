class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Visualize lining up strings
        # s = 'f o o'
        #      | | |
        # t = 'b a a'

        # Ex: {'f': 'b',
        #      'o': 'a'}
        charMap = {}

        for i in range(len(s)):
            if s[i] in charMap and t[i] != charMap[s[i]]:
                # Same chars in s line up with different chars in t
                return False

            # charMap.values() is still O(1) since there are only
            # a certain number of ascii characters
            if s[i] not in charMap and t[i] in charMap.values(): 
                # Diff chars map to same char
                return False
            
            charMap[s[i]] = t[i]
        
        return True
