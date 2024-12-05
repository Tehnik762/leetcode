# You are given an n x n 2D matrix representing an image,
# rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        temp = matrix.copy()
        for i in range(l):
            new_str = []
            for j in range(l-1,-1,-1):
                new_str.append(temp[j][i])
            matrix.pop(i)
            matrix.insert(i, new_str)
