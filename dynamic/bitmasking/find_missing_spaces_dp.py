from functools import cache
from typing import Set

"""
https://leetcode.com/problems/word-break/
"""


def _find_missing_spaces(s: str, vocabulary: Set[str]):
    """
    We create a DP storage of a length == len(s) + 1
    We use two pointers seeking for a word (i and j) such that word = s[i:j+1]
    We update DP to be True, when the word is in Vocabulary and is preceded with another existing word
        Such that `DP[j+1] in Vocabulary && DP[i] == True `
    We keep doing this until we mark last element of DP with True,
        which would mean the last word is found and it is preceded with valid words too
    """
    dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
    dp[0] = True
    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i] and s[i: j + 1] in vocabulary:
                dp[j + 1] = True
                if j + 1 == len(s) - 1:
                    return True
    return dp[-1]


def main():
    text = "javaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgood"
    # text = "javaisgood"
    vocabulary = {"java", "i", "is", "good"}
    print("Result: ", _find_missing_spaces(text, vocabulary))


if __name__ == '__main__':
    main()
