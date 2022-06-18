class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix); col = len(matrix[0])
        res = 0
        
        memo = {}
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def helper(i, j):
            if (i,j) in memo: return memo[(i,j)]
            path = 0
            for move in directions:
                r = i + move[0]
                c = j + move[1]
                if 0<=r<row and 0<=c<col and matrix[r][c] != '#' and matrix[r][c] > matrix[i][j]:
                    tmp = matrix[i][j]
                    matrix[i][j] = '#'
                    path = max(path, helper(r, c))
                    matrix[i][j] = tmp
            memo[(i,j)] = path + 1
            return memo[(i,j)]
        
        for i in range(row):
            for j in range(col):
                res = max(res, helper(i, j))
    
        return res