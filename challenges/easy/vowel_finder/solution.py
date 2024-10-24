def solution(s):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []

    # Iterate through each character in the string
    for i, char in enumerate(s):
        # If the lowercase char is in the vowel set, add it to the result
        if char.lower() in vowels:
            result.append(i)

    return result
