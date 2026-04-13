class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxRect = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                prev_i, prev_h = stack.pop()
                cur_rect = (i - prev_i) * prev_h
                maxRect = max(maxRect, cur_rect)
                start = prev_i
            stack.append((start, h))
        for i, h in stack:
            maxRect = max(maxRect, h * (len(heights) - i))
        return maxRect
