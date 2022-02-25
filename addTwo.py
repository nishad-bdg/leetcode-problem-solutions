nums = [3,2,4]
target = 6

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
      for i in range(len(nums)):
        for j in range(i+1, len(nums)):
          if nums[j] == target - nums[i]:
            print(i,j)


solution = Solution()
solution.twoSum(nums, target)