class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        binary search thru the rows
        check first and last element in each row
        if target is within this row, perfrom a binary search
        if is in that row
        return true
        otherwise false
        """

        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break

        if not top <= bottom:
            return False
        
        row = (top + bottom) // 2
        l = 0
        r = cols - 1
        while l<= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False