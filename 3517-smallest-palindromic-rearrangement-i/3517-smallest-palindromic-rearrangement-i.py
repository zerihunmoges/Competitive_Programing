from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        middle = ''
        if len(s)%2 != 0:
            middle = s[len(s)//2]

        t = ''
        s = sorted(list(s))
        i  = 0
        while i < len(s)-1:

            if s[i] == s[i+1]:
                t += s[i]
                i += 1

            i +=1

        return t + middle + ''.join(reversed(t))
