class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        index = 0
        for number in arr:
            if number == k:
                break
            if index == len(arr) - 1:
                index = -1
            else:
                index += 1
        return index
