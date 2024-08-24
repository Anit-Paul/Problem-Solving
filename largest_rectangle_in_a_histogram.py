class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [None for _ in range(len(heights))]
        right = [None for _ in range(len(heights))]
        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else len(heights)
            stack.append(i)
        maxi = 0
        for i in range(len(heights)):
            l = i - left[i]
            r = right[i] - i
            maxi = max(maxi, (l + r - 1) * heights[i])
        return maxi
