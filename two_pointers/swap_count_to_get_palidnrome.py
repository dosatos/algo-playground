from collections import Counter


def _is_palindrome(text: str) -> bool:
    number_of_evens = sum([1 for val in Counter(text).values() if val % 2 == 1])
    return True if number_of_evens == 1 or number_of_evens == 0 else False


def main():
    text = "mamad"
    if not _is_palindrome(text):
        return -1
    text = list(text)
    left, right = 0, len(text) - 1
    count = 0

    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            tmp = left
            while text[tmp] != text[right] and tmp < right:
                tmp += 1

            if tmp == right:
                text[right], text[right - 1] = text[right - 1], text[right]
                count += 1
            else:
                while tmp > left:
                    text[tmp], text[tmp - 1] = text[tmp - 1], text[tmp]
                    count += 1
                    tmp -= 1
                    print(text)
                assert text[tmp] == text[left]
    print(count, text)


if __name__ == '__main__':
    main()
