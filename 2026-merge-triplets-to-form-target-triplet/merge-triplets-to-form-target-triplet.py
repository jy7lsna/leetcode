class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merged = [0, 0, 0]

        for a, b , c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            merged[0] = max(merged[0], a)
            merged[1] = max(merged[1], b)
            merged[2] = max(merged[2], c)

        return merged == target