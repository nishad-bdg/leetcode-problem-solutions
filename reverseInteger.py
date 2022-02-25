class Solution:
  def reverseInteger(self, x: int) -> int:
    x = str(x)
    print(x[::-1])


sol = Solution()
sol.reverseInteger(-121)
