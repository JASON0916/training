"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""
__author__ = 'phoenix'


class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dungeon[m-1][n-1] = max(0-dungeon[m-1][n-1], 0)
        for i in range(m-2, -1, -1):
            dungeon[i][n-1] = max(dungeon[i+1][n-1] - dungeon[i][n-1], 0)
        for i in range(n-2, -1, -1):
            dungeon[m-1][i] = max(dungeon[m-1][i+1] - dungeon[m-1][i], 0)
        for x in range(m-2, -1, -1):
            for y in range(n-2, -1, -1):
                dungeon[x][y] = max(min(dungeon[x+1][y], dungeon[x][y+1]) - dungeon[x][y], 0)
        return dungeon[0][0] + 1


if __name__ == '__main__':
    matrix = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    o = Solution()
    print(o.calculateMinimumHP(matrix))
