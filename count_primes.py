class Solution:
    def countPrimes(self, n: int) -> int:
        helper = [1] * (n + 1)
        for i in range(2, n + 1):
            if i * i > n:
                break
            if helper[i] == 1:
                j = i * i
                while j <= n:
                    helper[j] = 0
                    j = j + i
        count = 0
        for i in range(2, n):
            if helper[i] == 1:
                count += 1
        return count
