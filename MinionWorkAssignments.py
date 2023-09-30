"""
Google FooBar Level 1 Task 1

Commander Lambda's minions are upset! They're given the worst jobs on the whole space station, and some of them are
starting to complain that even those worst jobs are being allocated unfairly. If you can fix this problem,
it'll prove your chops to Commander Lambda so you can get promoted!

Minions' tasks are assigned by putting their ID numbers into a list, one time for each day they'll work that task.
As shifts are planned well in advance, the lists for each task will contain up to 99 integers. When a minion is
scheduled for the same task too many times, they'll complain about it until they're taken off the task completely.
 Some tasks are worse than others, so the number of scheduled assignments before a minion will refuse to do a task
 varies depending on the task. You figure you can speed things up by automating the removal of the minions who have
 been assigned a task too many times before they even get a chance to start complaining.

Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n, and returns
that same list but with all the numbers that occur more than n times removed entirely. The returned list should
retain the same ordering as the original list - you don't want to mix up those carefully-planned shift rotations!
For instance, if data was [5, 10, 15, 10, 7] and n was 1, solution(data, n) would return the list [5, 15, 7] because 10
occurs twice, and thus was removed from the list entirely.
"""


class Solution(object):
    def solution(self, data, n):
        """
        Returns a list containing elements from the input data that appear
        less than or equal to 'n' times.

        O(n) complexity in both space and time.

        Parameters:
        ----------
        data (List[int]):
            A list of integers.
        n (int):
            The maximum number of times an integer is allowed to appear in the input data.

        Returns:
        -------
        List[int]:
            A list containing integers from the input data that appear less than or equal to 'n' times.
        """

        # initialise hashmap to store the number of times each number occurs
        occurrence_dict = {}

        # iterate through each number in the input array and count its frequency
        for num in data:
            if num not in occurrence_dict:
                occurrence_dict[num] = 1
            else:
                occurrence_dict[num] += 1

        # return the input list without values greater than a given frequency (n)
        return [num for num in data if occurrence_dict[num] <= n]


solution = Solution()

print(solution.solution([1, 2, 3], 0))  # expected output:
print(solution.solution([5, 10, 15, 10, 7], 1))  # expected output: [5, 15, 7]
print(solution.solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))  # expected output: [1, 4]
