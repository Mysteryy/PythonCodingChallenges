class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)

        result = ''

        i = a_len - 1
        j = b_len - 1
        carryover = 0

        while i >= 0 or j >= 0 or carryover:
            current_sum = (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0) + carryover
            carryover = current_sum // 2
            if current_sum > 1:
                current_sum -= 2

            result += str(current_sum)
            i -= 1
            j -= 1

        return result[::-1]
