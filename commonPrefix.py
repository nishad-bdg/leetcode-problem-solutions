
class Solution:
  def longestCommonPrefix(self, strs: str) -> str:
    if strs == []:
      return ''
    
    if len(strs) == 1:
      return strs[0]
    strs.sort()

    shortest = strs[0]
    prefix = ''

    for i in range(len(shortest)):
      if strs[len(strs) -1 ][i] == shortest[i]:
        prefix += strs[len(strs) -1][i]
      else:
        break
    return prefix


strs = ["flower", "flight", "flow"]

solution = Solution()
print(solution.longestCommonPrefix(strs))