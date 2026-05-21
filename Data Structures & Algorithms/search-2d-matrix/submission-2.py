class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            row = -1

            for i in range(0, len(matrix)-1):
                if matrix[i][0] == target:
                    return True
                elif matrix[i][0] < target and matrix[i+1][0] > target:
                    row = i
                    break
                else:
                    if i+1 == len(matrix):
                        row = i
                        break
            return self.search(matrix[row], target)
    def search(self, row, target):
        l,r = 0, len(row)-1
        found = False
        while (l <= r):
            mid = (l+r) // 2
            if(row[mid] > target):
                r = mid-1
            elif row[mid] < target:
                l = mid+1
            else:
               found = True
               return found
        return found
