class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            result = max([
                self._get_palindrome_size(s, i, i),
                self._get_palindrome_size(s, i, i + 1),
                result
            ], key=len)
        return result

    def _get_palindrome_size(self, text: str, left: int, right: int):
        size = 1
        while left >= 0 and right < len(text):
            if text[left] != text[right]:
                break
            left -= 1
            right += 1
            size += 2

        return text[left + 1:right]


def main():
    text = "racecar"
    s = Solution()
    print(s.longestPalindrome(text))


if __name__ == '__main__':
    main()