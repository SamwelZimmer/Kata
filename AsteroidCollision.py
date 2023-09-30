"""
https://leetcode.com/problems/asteroid-collision/

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning
right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        # initialise stack to store surviving asteroids
        stack = []

        # iterate through each asteroid
        for asteroid in asteroids:

            # if stack is empty or asteroid is moving to the right (positive value) then add asteroid
            if not stack or asteroid > 0:
                stack.append(asteroid)
                continue

            # loop until conditions are met
            while True:
                # get the size and direction of previous asteroid
                asteroid_prev = stack[-1]

                # if previous asteroid is going left (negative) it will not interact with any other asteroids
                if asteroid_prev < 0:
                    stack.append(asteroid)
                    break

                # if asteroids are of same size and opposite directions then they are both destroyed
                elif asteroid_prev == (-1 * asteroid):
                    stack.pop()
                    break

                # if asteroid at top of stack is bigger than incoming asteroid then it is not destroyed
                elif asteroid_prev > (-1 * asteroid):
                    break

                # if asteroid at top of stack is smaller than incoming asteroid it is destroyed
                else:
                    stack.pop()

                    # if stack is now empty then incoming asteroid is added to the stack
                    if not stack:
                        stack.append(asteroid)

                        break

        return stack


sol = Solution()

print(sol.asteroidCollision(asteroids=[5, 10, -5]))  # expected output: [5,10]
print(sol.asteroidCollision(asteroids=[8, -8]))  # expected output: []
print(sol.asteroidCollision(asteroids=[10, 2, -5]))  # expected output: [10]
print(sol.asteroidCollision(asteroids=[-2, -2, 1, -2]))  # expected output: [-2, -2, -2]

