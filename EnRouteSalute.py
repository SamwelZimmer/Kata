"""
Google Foobar Level 2 Task 2

Commander Lambda loves efficiency and hates anything that wastes time. The Commander is a busy lamb, after all! Henchmen
who identify sources of inefficiency and come up with ways to remove them are generously rewarded. You've spotted one
such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other -- one at
a time -- before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten
seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you could
save several collective hours of employee time per day. But first, you need to show the Commander how bad the problem
really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is
represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an
employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the
left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue
walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function solution(s) which takes a string representing employees walking along a hallway and returns the number
of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.
"""

# EASY FUCKIN MONEY BABY!!

class Solution(object):
    def solution(self, s):

        # create variables to store the number of people moving right and number of salute interactions
        right_movers, exchanges = 0, 0

        # iterate through each item in list
        for char in s:

            # add to counter if moving right
            if char == ">":
                right_movers += 1

            # if moving left but not at start of the input string increase exchange counters
            if char == "<" and right_movers != 0:
                exchanges += right_movers

        # each exchange consists of two salutes
        return exchanges * 2


solution = Solution()

print(solution.solution("--->-><-><-->-"))  # expected output: 10
print(solution.solution(">----<"))  # expected output: 2
print(solution.solution("<<>><"))  # expected output: 4

