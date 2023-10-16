"""
https://leetcode.com/problems/number-of-recent-calls/

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of
requests that has happened in the past 3000 milliseconds (including the new request).
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
"""

# In python, this has time complexity of O(n) because the list is not a real queue data structure,
# and .pop(0) requires each value to be shifted. If a real queue were used, would have a time complexity of O(1).


class RecentCounter(object):

    def __init__(self):
        self.requests = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        # add the new request to the end of the queue
        self.requests.append(t)

        # continue to iterate whilst que exists and until next item in queue is out range
        while self.requests and self.requests[0] < t - 3000:

            # remove item from front of queue
            self.requests.pop(0)

        # the items remaining in the queue are the ones in range (t - 3000 <= request <= t)
        return len(self.requests)


recentCounter = RecentCounter()
print(recentCounter.ping(1))       # expected output: 1
print(recentCounter.ping(100))     # expected output: 2
print(recentCounter.ping(3001))    # expected output: 3
print(recentCounter.ping(3002))    # expected output: 3
