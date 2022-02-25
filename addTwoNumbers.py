class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0


solution = Solution()
print(solution.addDigits(0))