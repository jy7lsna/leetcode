class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            key = tuple(freq)
            groups[key].append(s)
        
        return list(groups.values())


# eat = e-1, a-1, t-1
# tea = t-1, e-1, a-1
# tan = t-1, a-1, n-1
# ate = a-1, t-1, e-1
# nat = n-1, a-1, t-1
# bat = b-1, a-1, t-1