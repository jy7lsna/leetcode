class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        count = Counter(hand)

        for card in sorted(count):
            if count[card] > 0:
                needed = count[card]
                for i in range(groupSize):
                    if count[card + i] < needed:
                        return False
                    count[card + i] -= needed
        return True