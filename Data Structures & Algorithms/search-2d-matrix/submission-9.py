class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr_l, arr_r = 0, len(matrix) - 1

        while arr_l <= arr_r:
            arr_mid = (arr_l + arr_r) // 2
            if target < matrix[arr_mid][0]:
                arr_r = arr_mid - 1
            elif target > matrix[arr_mid][-1]:
                arr_l = arr_mid + 1
            else:
                l = 0
                r = len(matrix[arr_mid]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if target < matrix[arr_mid][mid]:
                        r = mid - 1
                    elif target > matrix[arr_mid][mid]:
                        l = mid + 1
                    else:
                        return True
                return False
        return False


"""
Goal: check if target exists in matrix in O(log(m*n))
- binary search to find the array the target is in
- binary search to find the position the target is in
"""