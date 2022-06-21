
import random

class Solution:


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

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()