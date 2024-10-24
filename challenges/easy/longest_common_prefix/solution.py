class Solution(object):
    def solution(self, strs: list):
        input_len = len(strs)

        # Early return conditions to prevent errors and save time in certain cases
        if input_len == 0:
            return ""
        elif input_len == 1:
            return strs[0]

        # Sort the input str list, then get the first and last elements, at this point we have at least 2 elements
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        prefix = ""
        # Iterate each index and char of the shortest element
        for i, char in enumerate(min(first, last)):
            # Characters are not equal, stop looking
            if last[i].lower() != char.lower():
                break
            # Add to our longest prefix
            prefix += char

        return prefix
