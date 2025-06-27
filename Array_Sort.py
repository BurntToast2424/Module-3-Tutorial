class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        zerocount = 0
        onecount = 0
        for number in arr:
            if number == 0:
                zerocount += 1
            if number == 1:
                onecount += 1
        for number in range(len(arr)):
            if zerocount != 0:
                arr[number] = 0
                zerocount -= 1
            elif onecount != 0:
                arr[number] = 1
                onecount -= 1
            else:
                arr[number] = 2
