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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        maxi = 0
        for i in range(col):
            count = 0
            for j in range(row):
                if matrix[j][i] == "1":
                    count = count + int(matrix[j][i])
                    matrix[j][i] = count
                else:
                    matrix[j][i] = int(matrix[j][i])
                    count = 0
        print(matrix)
        for i in matrix:
            maxi = max(maxi, self.largestRectangleArea(i))
        return maxi
