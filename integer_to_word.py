from collections import defaultdict
class Solution:
    def helper(self, dig, l):
        if int(dig) == 0:
            return ""
        if l == 0:
            return ""
        if dig[0] == "0":
            return self.helper(dig[1:], l - 1)
        word = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }
        s = ""
        if l == 3:
            s += word[int(dig[0])] + " Hundred " + self.helper(dig[1:], l - 1)
        elif l == 2:
            if dig[0] == "1":
                return word[int(dig[0:])].strip()
            else:
                s += word[int(dig[0]) * 10] + " " + self.helper(dig[1:], l - 1)
        else:
            return word[int(dig[0])]
        return s.strip()

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        map = defaultdict()
        num = str(num)
        j = len(num) - 1
        i = j - 2
        count = 0

        while i >= 0:
            map[count] = num[i : j + 1]
            j -= 3
            i -= 3
            count += 1
        if j >= 0:
            map[count] = num[: j + 1]

        word = {0: "", 1: " Thousand ", 2: " Million ", 3: " Billion "}
        ans = ""
        for key, value in map.items():
            res = self.helper(value, len(value))
            if len(res) > 0:
                ans = res + word[key] + ans
        return ans.strip()
