class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        maxFreq = 0
        freq = [0] * 26
        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            freq[idx] += 1
            maxFreq = max(maxFreq, freq[idx])

            while (r - l + 1) - maxFreq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest