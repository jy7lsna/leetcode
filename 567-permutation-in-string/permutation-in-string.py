class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord('a')] += 1
        
        n = len(s1)
        window = [0] * 26
        for i in range(n):
            window[ord(s2[i]) - ord('a')] += 1
        
        if window == freq:
            return True
        
        for r in range(n, len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[r-n]) - ord('a')] -= 1

            if window == freq:
                return True
        
        return False
        