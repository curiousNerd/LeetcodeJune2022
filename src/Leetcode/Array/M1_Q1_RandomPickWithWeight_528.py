
import random

class Solution1:


    '''
    This is a Brute Force Solution
    T : O(N) : N is the sum of all elements in the array [Each element can be 10^5 and total Length of the array be 10^4, So N can reach 10^9]
    S : O(N)
    '''

    def __init__(self, arr):

        self.arr = arr
        self.sum = 0
        for idx in range(0, len(arr)):
            self.sum += arr[idx]


    def pickIndex(self) -> int:

        arr = self.arr
        new_arr = [None] * self.sum
        pointer = 0
        for idx in range(0, len(arr)):
            counter = 0
            while counter != arr[idx]:
                new_arr[counter + pointer] = idx
                counter += 1

            pointer += counter

        return random.choice(new_arr)

class Solution2:

    '''
    This is Linear Solution
    T : O(n) : Can reach 10^9
    S : O(n) : Can reach 10^9
    '''

    def __init__(self, arr):

        self.arr = arr
        self.cum_arr = [None] * len(arr)
        self.cum_sum = 0
        for idx in range(0, len(arr)):
            self.cum_sum += arr[idx]
            self.cum_arr[idx] = self.cum_sum


    def pickIndex(self) -> int:

        rd = random.randrange(0,self.cum_sum)

        for idx in range(0, len(self.cum_arr)):

            if rd < self.cum_arr[idx]:
                return idx



class Solution:

    def __init__(self, arr: int):

        self.arr = arr
        self.cum_arr = [None] * len(arr)
        self.cum_sum = 0
        for idx in range(0, len(arr)):
            self.cum_sum += arr[idx]
            self.cum_arr[idx] = self.cum_sum


    def pickIndex(self) -> int:

        lo = 0
        hi = len(self.cum_arr) - 1

        rd = random.randrange(0, self.cum_sum)
        res = -1
        while lo <= hi:

            mid = lo + (hi - lo)//2

            if rd < self.cum_arr[mid]:
                res = mid
                hi = mid - 1

            else:
                lo = mid + 1

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()