class Solution:
    def countCommas(self, n: int) -> int:

        # 100,450,000,002
        # 999,999,999


        count = 0
        current_commas = len(str(n))//3 if len(str(n))//3 != len(str(n))/3 else len(str(n))//3-1
        while current_commas >= 1:

            next_n = int('999'*(current_commas))

            total_nums = n - max(next_n, 999)

            count += total_nums*current_commas
            current_commas -= 1
            n = next_n

        return count


        
        