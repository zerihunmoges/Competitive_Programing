import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        n = 2*n
        total = n*(n+1)//2
        sumOdd= (total-n//2)//2
        sumEven = total-sumOdd
        return math.gcd(sumEven, sumOdd)


        

        