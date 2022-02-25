class Solution:
   def romanToInt(self, s: str) -> int:
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

      prev = 0
      curr = 0
      total = 0

      for i in range(len(s)):
         curr = roman[s[i]]

         if curr > prev:
            total = total + curr - 2 * prev
         else:
            total += curr
         prev = curr
      return total


sol = Solution()

s = input('')
print(sol.romanToInt(s.upper()))
