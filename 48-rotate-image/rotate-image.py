class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        result = [[0 for _ in range(n)]for _ in range(n)]
        for i in range(0,n):
            for j in range(0,n):
                result[j][(n-1)-i] = matrix[i][j]
        matrix[:]=result


        