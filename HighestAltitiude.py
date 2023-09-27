"""
https://leetcode.com/problems/find-the-highest-altitude/

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i
and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""


class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        # initialise variables to store the current and highest amplitudes
        altitude = 0
        highest_altitude = altitude

        # iterate through the lists of height changes
        for height in gain:

            # alter the current altitude based on the height change
            altitude += height

            # reassign the highest altitude
            highest_altitude = max(highest_altitude, altitude)

        return highest_altitude


sol = Solution()

print(sol.largestAltitude(gain=[-5, 1, 5, 0, -7]))  # expected output: 1
print(sol.largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]))  # expected output: 0
