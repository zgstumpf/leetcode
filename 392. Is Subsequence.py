class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Empty string is always subsequence
        if s == "":
            return True

        i = 0
        for j in range(len(t)):
            # Good - t's char matches s's char.
            # Now start checking next char in s for match.
            if t[j] == s[i]:
                i += 1

                # All chars in s have been processed
                if i == len(s):
                    return True
        # We looked at all chars in t and never found subsequence
        return False
