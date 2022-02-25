s = "{(){}"
stack = []

closeToOpen = {')': '(', '}': '{', ']': '['}


class Solution:
    def isValid(self, s: str) -> bool:
      for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
        else:
          stack.append(c)
      return True if not stack else False

  
sol = Solution()
print(sol.isValid(s))
