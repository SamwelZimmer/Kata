"""
Google Foobar Level 3 Task 1

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to
the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets
a report every day that includes the locks' access codes, but only the Commander knows how to figure out which of
several lists contains the access codes. You need to find a way to determine which list contains the access codes once
you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access codes
are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple (x, y, z) where x
divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number
of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5
passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of
(li, lj, lk) where the list indices meet the requirement i < j < k. The length of l is between 2 and 2000 inclusive.
The elements of l are between 1 and 999999 inclusive. The solution fits within a signed 32-bit integer. Some lists are
purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.
"""


class Solution(object):
    def solution(self, l):
        """
        time complexity: O(n**2)
        space complexity: O(n)
        """

        # length of the input array
        n = len(l)

        # to store the number of divisors to the left of each value in input array
        divisors = [0] * n

        # iterate through each value in the input array
        for i in range(n):

            # set a variable to keep track of how many divisors each value has
            count = 0

            # iterate between start of the array and current value (i)
            for j in range(i):

                # if values are divisors, add to count
                if l[i] % l[j] == 0:
                    count += 1

            # update list to store count value
            divisors[i] = count

        # variable to store the output value
        result = 0

        # iterate between the second and second-last item in input array
        for j in range(1, n - 1):

            # iterate between the value to the right of j and the end of the input array
            for k in range(j + 1, n):

                # if values are divisible then number of triples but by increases by value store in divisor counts
                if l[k] % l[j] == 0:
                    result += divisors[j]

        return result


solution = Solution()

print(solution.solution([1, 1, 1]))  # expected output: 1
print(solution.solution([1, 2, 3, 4, 5, 6]))  # expected output: 3