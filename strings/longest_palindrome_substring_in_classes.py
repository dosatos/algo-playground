from typing import List
from pprint import pprint


class LongestPalindromeString:
    def find(self, text: str):
        raise NotImplementedError("Must be implemented")


class NaiveLongestPalindromeString(LongestPalindromeString):
    def _is_palindrome(self, substring: str) -> bool:
        return substring == substring[::-1]

    def find(self, text: str) -> str:
        longest = ""
        for left in range(len(text)):
            for right in range(left, len(text)):
                substring = text[left:right+1]
                if self._is_palindrome(substring):
                    longest = max(longest, substring, key=lambda x: len(x))
        return longest


class _DynamicLpsSolution:
    def __init__(self, text: str):
        self.text = text
        self.table = [[0 for _ in range(len(text))] for _ in range(len(text))]
        self.longest = ""

    def find(self) -> str:
        for increment in range(len(self.text)):
            self._process_diagonal(increment)
        return self.longest

    def _is_palindrome_dynamic(self, start: int, end: int) -> bool:
        """
        Check is the substring edges are equal 
        AND 
        if subsring excluding the edges is palindrome (gets from table)
        """
        if self.text[start] == self.text[end]:
            if end - start <= 1:
                return 1
            if self.table[start+1: end]:
                return 1
        return 0

    def _process_diagonal(self, increment: int):
        for row in range(len(self.text)):
            col = row + increment
            try:
                if self._is_palindrome_dynamic(row, col):
                    self.longest = max(self.longest, self.text[row: col+1], key=lambda x: len(x))
                    self.table[row][col] = 1
                else:
                    self.table[row][col] = 0
            except IndexError:
                continue


class DynamicLongestPalindromeString(LongestPalindromeString):
    def find(self, text: str):
        return _DynamicLpsSolution(text).find()


def main():
    text = "a"
    print("Naive:", NaiveLongestPalindromeString().find(text), "Dynamic:", DynamicLongestPalindromeString().find(text))
    assert(NaiveLongestPalindromeString().find(text) == DynamicLongestPalindromeString().find(text))
    print("Longest palindrome is:", DynamicLongestPalindromeString().find(text))


if __name__ == "__main__":
    main()
