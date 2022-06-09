from typing import List, Optional
from pprint import pprint


def _is_palindrome(substring: str) -> bool:
    return substring == substring[::-1]
    

def get_longest_substring_palindrome_naive(text: str):
    longest = ""
    for left in range(len(text)):
        for right in range(left + 1, len(text)):
            substring = text[left:right]
            if _is_palindrome(substring):
                longest = max(longest, substring, key=lambda x: len(x))
    return longest


def _is_palindrome_dynamic(text: str, table: List[List[int]], start: int, end: int) -> bool:
    if text[start] == text[end]:
        if end - start <= 1:
            return 1
        if table[start+1: end]:
            return 1
    return 0


def _process_diagonal(text: str, increment: int, table: List[List[int]]):
    for start in range(len(text)):
        end = start + increment
        try:
            table[start][end] = _is_palindrome_dynamic(text, table, start, end)
        except IndexError:
            continue


def _get_longest(table: List[List[int]], text: str):
    row, col = 0, len(table) - 1
    queue = [(row, col)]
    while queue:
        if table[row][col]:
            return text[row: col+1]
        row, col = queue.pop(0)
        queue.append((row, col - 1))
        queue.append((row + 1, col))
        queue.append((row + 1, col - 1))


def _init_table(text: str) -> List[List[int]]:
    return [[0 for _ in range(len(text))] for _ in range(len(text))]


def get_longest_palindrome_substring(text: str) -> Optional[str]:
    table = _init_table(text)
    for increment in range(len(text)):
        _process_diagonal(text, increment, table)
    return _get_longest(table, text)


def main():
    text = "baabaac"
    assert(get_longest_substring_palindrome_naive(text) == get_longest_palindrome_substring(text))
    print("Longest palindrome is:", get_longest_palindrome_substring(text))


if __name__ == "__main__":
    main()
