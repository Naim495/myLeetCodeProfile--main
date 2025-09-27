// 1st mathod 
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # calculate area
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # move the smaller pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
2nd mathod

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            # Move the smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

  3rd 
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L = 0
        R = len(height)-1
        max_area = float('-inf')
        while L<R:
            area = min(height[L],height[R]) * (R-L)
            max_area = max(max_area,area)
            if height[L]<height[R]:
                L +=1
            else:
                R -=1
