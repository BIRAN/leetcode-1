#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (52.88%)
# Likes:    1639
# Dislikes: 267
# Total Accepted:    171.6K
# Total Submissions: 323.5K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        nRow = len(board)
        nCol = len(board[0])
        count = 0
        for i in range(nRow):
            for j in range(nCol):
                count = self.getNLive(i,j,nRow,nCol, board)
                if board[i][j]==1:
                    if count<2 or count > 3:
                        # from 1 to 0, assign 3
                        board[i][j]=3
                else:
                    if count == 3:
                        # fomr 0 to 1, assign 2
                        board[i][j]=2
        for i in range(nRow):
            for j in range(nCol):
                if board[i][j]==3:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=1

    def getNLive(self, ir, ic, nRow, nCol, matrix):
        rStart = max(ir-1, 0)
        cStart = max(ic-1, 0)
        rEnd = min(ir+1, nRow-1)
        cEnd = min(ic+1, nCol-1)
        count = 0
        for i in range(rStart, rEnd+1):
            for j in range(cStart, cEnd+1):
                if matrix[i][j]%2==1:
                    count+=1
        # if matrix[ir][ic]==1 : minus 1 
        # only need 8 neighbours not itself
        if matrix[ir][ic]==1:
            count-=1
        return count
        

# @lc code=end

