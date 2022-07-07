"""
    * Input : Array, target
    * Output : Array

    * Exp : Given an input array - sorted in ascending order - return array of 2 indexes where arr[i] + arr[j] = target

    * Questions / Conditions :

        * Is the array sorted :  Yes
        * Will there be always a solution : Yes
        * Will there be more than one solution : No - Exactly one Solution


"""


class Solution:

    """

    T: O(N^2)
    S: O(1)

    """

    def twoSumII_bruteForce(self, arr, target):

        for i in range(0, len(arr)):

            for j in range(i + 1, len(arr)):

                if arr[i] + arr[j] == target:
                    return [i + 1, j + 1]

        return []

    """

    T: O(N)
    S: O(1)

    """


    def twoSum_Linear(self, arr: List[int], target: int) -> List[int]:

        # Base Condition

        if arr is None or len(arr) == 0:
            return []

        # Implementation

        lo = 0
        hi = len(arr)-1

        while lo < hi:

            if arr[lo] + arr[hi] < target :
                ## add bigger numbers : Move right : lo++

                lo += 1

            elif arr[lo] + arr[hi] > target :
                ## add smaller number : Move left : hi --

                hi -= 1

            else:
                ## Because there will be always some solution : this is it

                return[lo+1, hi+1]

        return []
