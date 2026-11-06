class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            mostheaviest = stones.pop()
            secondheaviest = stones.pop()
            # print(mostheaviest,secondheaviest)
            if mostheaviest == secondheaviest:
                continue
            stones.append(mostheaviest-secondheaviest)
            stones.sort()
        
        return stones[0] if len(stones) > 0 else 0

