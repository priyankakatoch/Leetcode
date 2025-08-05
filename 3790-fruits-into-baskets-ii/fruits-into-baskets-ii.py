from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c = 0
        n = len(fruits)
        m = len(baskets)
        used = [False] * m 

        for i in range(n):
            for j in range(m):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True
                    c += 1
                    break
        
        return n - c  
