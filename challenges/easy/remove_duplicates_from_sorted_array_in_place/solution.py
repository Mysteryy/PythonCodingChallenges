class Solution(object):
    def removeDuplicates(self, input_a):
        k = 1
        for i in range(1, len(input_a)):
            if input_a[i] != input_a[i - 1]:
                input_a[k] = input_a[i]
                k += 1
        del input_a[k:]  # Not required by the challenge, but makes for a nicer solution
        return k