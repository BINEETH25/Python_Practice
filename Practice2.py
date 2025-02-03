'''
nums = [3, 3]#[3, 2, 4]#[2, 7, 11, 15]
target = 6 #6 #9
y = len(nums)
for i in range(y):
	for j in range(i+1, y):
		c = nums[i] + nums[j]
		if target == c:
			print(i,j)
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        y = len(nums)
        for i in range(y):
            for j in range(i+1, y):
                c = nums[i] + nums[j]
                if target == c:
                    print(i,j)
                    
solution = Solution()
solution.twoSum([2,7,11,15], 9)