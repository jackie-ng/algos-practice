class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if the matrix is empty or if the first row is empty
        if not matrix or not matrix[0]:
            # If empty, the target cannot exist, so return False
            return False

        # Get the number of rows (m) and columns (n) in the matrix
        m = len(matrix)  # Total number of rows
        n = len(matrix[0])  # Total number of columns (assuming all rows have equal length)

        # Initialize binary search boundaries for rows
        top = 0  # Start from the first row
        bottom = m - 1  # End at the last row

        # Perform binary search to find the correct row where the target might be
        while top <= bottom:
            mid_row = (top + bottom) // 2  # Compute the middle row index
            
            # Check if the target is within the range of the current row
            if matrix[mid_row][0] <= target <= matrix[mid_row][n - 1]:
                # If yes, break out of the loop to search within this row
                break
            # If the target is larger than the last element in the current row
            elif matrix[mid_row][n - 1] < target:
                # Search the upper half (rows after mid_row)
                top = mid_row + 1
            else:
                # Otherwise, search the lower half (rows before mid_row)
                bottom = mid_row - 1

        # Now, perform binary search within the selected row
        l = 0  # Start from the first column
        r = n - 1  # End at the last column
        row = matrix[mid_row]  # Store the row for easier access

        while l <= r:
            mid = (l + r) // 2  # Compute the middle column index
            
            # If the middle element is the target, return True
            if row[mid] == target:
                return True
            # If the target is larger than the middle element, search the right half
            elif row[mid] < target:
                l = mid + 1
            # If the target is smaller, search the left half
            else:
                r = mid - 1

        # If the loop completes without finding the target, return False
        return False