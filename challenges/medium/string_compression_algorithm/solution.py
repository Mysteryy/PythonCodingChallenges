from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # Early returns for sanity check and error prevention
        if not chars:
            return 0
        elif len(chars) == 1:
            return 1

        prev_char = None  # Track the prev char so we know when a char change occurs
        current_counter = 0  # Counter for the current character
        current_index = 0  # Used to track the index where we will insert (overwrite) elements in the chars list

        # Iterate all chars in the input only once
        for i, char in enumerate(chars):
            current_counter += 1  # Increment the counter

            # We have finished our max sequence for the current character, or we are on the last character so we need to handle it
            if prev_char is not None and (char != prev_char or i == len(chars) - 1):
                # Insert prev char in the right spot in our list
                chars[current_index] = prev_char

                # If we are on the last index and this char is the same as prev, add one more to current counter (handle edge case)
                if i == len(chars) - 1 and prev_char == char:
                    current_counter += 1

                # If there is > 1 instance, we need to add a counter after it in the list
                if current_counter - 1 > 1:
                    # Add the counter to list after the character. If counter is multiple digits, we need to insert one digit per index.
                    counter_str = str(current_counter - 1)
                    for s in counter_str:
                        current_index += 1
                        chars[current_index] = s

                # We are on the last char, and it's not the same as prev char, insert it (edge case since loop will not run again to handle this char)
                if i == len(chars) - 1 and prev_char != char:
                    current_index += 1
                    chars[current_index] = char

                current_index += 1

            if prev_char != char:
                # Reset our counter, were on a new character now
                current_counter = 1

            prev_char = char

        return current_index
