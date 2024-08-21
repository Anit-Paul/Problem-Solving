class Solution:
    def left_min(self, arr):
        lm = [None for _ in range(len(arr))]
        stack = []
        for i in range(0, len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            lm[i] = stack[-1] if stack else -1
            stack.append(i)
        return lm

    def right_min(self, arr):
        lm = [None for _ in range(len(arr))]
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            lm[i] = stack[-1] if stack else len(arr)
            stack.append(i)
        return lm

    def sumSubarrayMins(self, arr: List[int]) -> int:
        lm = self.left_min(arr)
        rm = self.right_min(arr)
        count = 0
        for i in range(len(arr)):
            l = i - lm[i]
            r = rm[i] - i
            count = (count + (l * r * arr[i])) % ((10**9) + 7)
        return count
