class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxFreq = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
        
            res = max(res, r - l + 1)
        return res 