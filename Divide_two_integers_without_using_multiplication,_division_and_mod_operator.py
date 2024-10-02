class Solution:
    def divide(self, d1: int, d2: int) -> int:
        res = 0
        flag = False
        if (d1 < 0 and d2 < 0) or (d1 >= 0 and d2 > 0):
            flag = True
        d1 = abs(d1)
        d2 = abs(d2)
        while d1 >= d2:
            count = 0
            while (d2 << (count + 1)) <= d1:
                count += 1
            res += 1 << (count)
            d1 -=  (d2 << (count))
        if flag == False:
            res = -res
        if res >= (1 << 31) - 1:
            return (1 << 31) - 1
        if res <= -(1 << 31):
            return -(1 << 31)
        return res
