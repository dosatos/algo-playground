def _get_step_table(pattern):
    # init
    unique_letters = {letter: 0 for letter in set(pattern)}
    
    # assign except for the last
    for idx, letter in enumerate(pattern[:-1]):
        unique_letters[letter] = len(pattern) - 1 - idx
    
    # assign the last
    last_letter = pattern[-1]
    unique_letters[last_letter] = len(pattern)

    return unique_letters


def _compare(pattern: str, word: str):
    print(f"Comaring {pattern} and {word}")
    index = len(pattern) - 1
    while index >= 0:
        if pattern[index] == word[index]:
            index -= 1
            _compare.comparison_count += 1
        else:
            _compare.comparison_count += 1
            break
    return index


def _get_step_size(step_table, letter, pattern):
    step_size = step_table.get(letter)
    print(f"Moving by {step_size}")
    return step_size if step_size else len(pattern)


def _find_naive(pattern: str, text: str):
    step_table = _get_step_table(pattern)
    # print(f"Table: {step_table}")
    pos = 0
    while pos <= len(text) - len(pattern):
        word = text[pos:pos+len(pattern)]
        mismatch_index = _compare(pattern, word)
        if mismatch_index == -1:
            return pos
        pos += _get_step_size(step_table, word[mismatch_index], pattern)


def _find_boyer_moore(pattern: str, text: str):
    pos = 0
    while pos <= len(text) - len(pattern):
        word = text[pos:pos+len(pattern)]
        if word == pattern:
            return pos
        pos += 1


def main():
    test_cases = [
        # ("TRUST HARD TOOTH BRUSHES", "TOOTH"),
        # ("abababababababababababababababababababababababab", "abaa"),
        ("cxaaabcaaaabcaaaabcaaaabcaaaabcaaaabcaaaabbaaaab", "baaaab"),
        # ("ainaisesti-ainainen", "ainainen"),
    ]
    for text, pattern in test_cases:
        _compare.comparison_count = 0
        print(f"\nLooking for {pattern} in {text}")
        position = _find_boyer_moore(pattern, text)
        assert(position == _find_naive(pattern, text))
        print(position)
        print(f"text: {len(text)}, pattern: {len(pattern)}, comparison: {_compare.comparison_count}")


if __name__ == "__main__":
    main()
