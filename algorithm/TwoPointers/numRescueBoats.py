# 对应leetcode 881
'''
    给定一个列表包含i个人，第i个人的体重为people[i]，每艘船最大承载为limit；
    每艘船最多可同时载两人，但前提条件为这些人的重量之和最多为limit；
    返回把每个人都载走所需的最小船数量。
'''
from typing import List
class Solution:
    def __init__(self) -> None:
        self.result = 0
    
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            self.result += 1
        return self.result

if __name__ == "__main__":
    s = Solution()
    print(s.numRescueBoats([3,2,2,1], 3))