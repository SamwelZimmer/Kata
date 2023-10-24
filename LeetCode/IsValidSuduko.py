"""
https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        squares_dict = {
            1: {"rows": [0, 1, 2], "cols": [0, 1, 2], "values": []},
            2: {"rows": [0, 1, 2], "cols": [3, 4, 5], "values": []},
            3: {"rows": [0, 1, 2], "cols": [6, 7, 8], "values": []},
            4: {"rows": [3, 4, 5], "cols": [0, 1, 2], "values": []},
            5: {"rows": [3, 4, 5], "cols": [3, 4, 5], "values": []},
            6: {"rows": [3, 4, 5], "cols": [6, 7, 8], "values": []},
            7: {"rows": [6, 7, 8], "cols": [0, 1, 2], "values": []},
            8: {"rows": [6, 7, 8], "cols": [3, 4, 5], "values": []},
            9: {"rows": [6, 7, 8], "cols": [6, 7, 8], "values": []},
        }

        # function to determine whether each row is valid
        def check_row(row):
            row_nums = [int(char) for char in row if char.isalnum()]
            return len(set(row_nums)) == len(row_nums)

        # iterate through each row and return if invalid
        for row in board:
            if not check_row(row):
                return False

        # pivot the board so columns become rows
        pivoted_board = [list(tup) for tup in zip(*board)]

        # iterate through each column and return if invalid
        for col in pivoted_board:
            if not check_row(col):
                return False

        for key in squares_dict.keys():
            for row in squares_dict[key]["rows"]:
                for col in squares_dict[key]["cols"]:
                    char = board[row][col]
                    if char.isalnum():
                        squares_dict[key]["values"].append(board[row][col])

            if not len(squares_dict[key]["values"]) == len(set(squares_dict[key]["values"])):
                return False

        return True

    def betterSolution(self, board):

        # create hashmaps, with the value being a set, for the rows, cols and 3x3 squares
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (row / 3, col / 3)

        # iterate through the board
        for row in range(9):
            for col in range(9):

                # skip to next iteration if space is empty
                if board[row][col] == ".":
                    continue

                # if item is already in a dictionary then position is invalid
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row // 3, col // 3)]):
                    return False

                # update the hashmaps
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])

        return True



sol = Solution()

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(sol.betterSolution(board=board))  # expected: True

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(sol.betterSolution(board=board))  # expected: False

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    [".",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(sol.betterSolution(board=board))  # expected: False
