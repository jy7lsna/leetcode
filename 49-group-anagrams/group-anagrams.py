class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq)
            groups[key].append(word)
        return list(groups.values())



