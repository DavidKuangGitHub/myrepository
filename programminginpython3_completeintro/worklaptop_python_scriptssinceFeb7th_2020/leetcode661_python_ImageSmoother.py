"""leetcode661_python_ImageSmoother.py
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to
make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding
cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.
Example1. Input:
[[1,1,1],  (0,2)
 [1,0,1],  (0,1)
 [1,1,1]]  (0,0)-(1,0)-(2,0)
Output:
[[0,0,0],
 [0,0,0],
 [0,0,0]] Because here is the explanation:
For the point (0,0),(0,2),(2,0),(2,2): floor(3/4) = floor(0.75)=0
For the point (0,1),(1,0),(1,2),(2,1): floor(5/6) = floor(0.83333333...)=0
For the point (1,1): floor(8/9) = floor(0.88888...)=0
Note: 1. The value in the given matrix is in the range of [0,255]
2. The length and width of the given matrix are in the range of [1,150]
"""
import copy
class ImageSmoother(object):
    def convert(self,M):
        n = len(M)
        m = len(M[0])
        M2 = copy.deepcopy(M)
        for i in range(n):
            M[i].append(-1)
        M.append([-1]*(m+1))
        for i in range(n):
            for j in range(m):
                tmp = [M[i-1][j-1],M[i][j-1],M[i+1][j-1],M[i-1][j],M[i+1][j],M[i-1][j+1],M[i][j+1],M[i+1][j+1]]
                c = tmp.count(-1)
                M2[i][j] += sum(tmp) + c
                M2[i][j] = int(M2[i][j]/(9-c))
        return M2

"""matrix = []
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)"""

instanceofImageSmoother = ImageSmoother()
myx=[[1,1,1],[1,0,1],[1,1,1]]
print("Result of ImageSmoother =", instanceofImageSmoother.convert(myx))