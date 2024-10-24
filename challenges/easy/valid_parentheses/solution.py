
class Solution(object):

    def isValid(self, s: str) -> bool:
        # Early check to return False - If len of s is not divisible by 2 then we know we have an unmatched pair.
        if len(s) % 2 != 0:
            return False

        paren_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        # Track a set of valid characters to ensure no invalid characters are detected in the string
        valid_chars = set()
        for key, value in paren_map.items():
            valid_chars.add(key)
            valid_chars.add(value)

        stack = []
        for char in s:
            if char not in valid_chars:
                return False # Invalid character (not explicitly required by the challenge, but good practice to cover edge cases)

            if char in paren_map: # This is an opening bracket, so push it on the stack and check for closing bracket in a future iteration
                expected_closing_bracket = paren_map[char]
                stack.append(expected_closing_bracket)
            elif len(stack) > 0:
                expected_closing_bracket = stack.pop()
                if char != expected_closing_bracket:
                    return False
            else: # We have a closing bracket but there was no opening bracket to match it previously (i.e. the closing bracket came before the opening bracket)
                return False

        # If there are no expected closing brackets on the stack, return True, else False because we are missing closing brackets
        return len(stack) == 0