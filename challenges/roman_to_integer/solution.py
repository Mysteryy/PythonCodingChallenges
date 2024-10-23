class Solution(object):
    numeral_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def solution(self, input_a):
        result = 0
        # Track prev value for comparison as we iterate
        prev_value = None
        for char in input_a:
            if char.upper() in self.numeral_map:
                current_value = self.numeral_map[char]
                result += current_value
                if prev_value and prev_value < current_value:
                    result = result - (2 * prev_value)
                prev_value = current_value
            else:  # Invalid input
                print(f'Invalid character in input: char={char}    input={input_a}')
                return 0

        return result
