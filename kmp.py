class Solution:
    def compute_lps(self, arr):
        lps = [0] * len(arr)
        prefix = 0
        suffix = 1
        while suffix < len(arr):
            if arr[suffix] == arr[prefix]:
                lps[suffix] = prefix + 1
                prefix += 1
                suffix += 1
            else:
                if prefix == 0:
                    suffix += 1
                else:
                    prefix = lps[prefix - 1]
        return lps

    def kmp(Self, a, b, lps):
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
        if j != len(b):
            return -1
        return i - j

    def strStr(self, a: str, b: str) -> int:
        if len(a) < len(b):
            return -1
        lps = self.compute_lps(b)
        return self.kmp(a, b, lps)
