def triple_is_zigzag(numbers):
    if len(numbers) == 3:
        return 1 if (numbers[0] < numbers[1] > numbers[2]) or (numbers[0] > numbers[1] < numbers[2]) else 0

    return False


def solution(numbers):
    result = []

    for i in range(0, len(numbers) - 2):
        result.append(triple_is_zigzag(numbers[i:i + 3]))

    return result
