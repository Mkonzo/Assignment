"""
Task 2: char_frequency
Count letters case-insensitively in O(n).
"""


def char_frequency(text):
    counts = {}
    for ch in text:
        if ch.isalpha():                # only count letters
            ch = ch.lower()             # case-insensitive
            counts[ch] = counts.get(ch, 0) + 1
    return counts


if __name__ == "__main__":
    sample = "Mississippi River, USA!"
    result = char_frequency(sample)
    for letter in sorted(result):
        print(f"{letter}: {result[letter]}")
        