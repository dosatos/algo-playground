from typing import Set, List
from tqdm import tqdm


def _get_combinations(text: str) -> int:
    """
    Space, O1
    Time: O(2^N)
    """
    all_spaced = "".join(['1'] * len(text))
    for mask in range(int(all_spaced, 2), 0, -1):
        yield mask


def _find(mask, text, vocabulary):
    result = set()
    word = ""
    for j in range(len(text)):  # O(N)
        word += text[j]
        if mask & 1 << j:
            result.add(word)
            if word not in vocabulary:
                return
            word = ""
    return result


def _find_missing_spaces(text: str, vocabulary: Set[str]):
    for mask in tqdm(_get_combinations(text, vocabulary)):  # O(2^N) combinations
        result = _find(mask, text, vocabulary)  # O(N*2^N)
        if result:
            return result


def main():
    text = "javaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgoodjavaisgood"
    # text = "javaisgood"
    vocabulary = {"java", "i", "is", "good"}
    print("Result: ", _find_missing_spaces(text, vocabulary))


if __name__ == '__main__':
    main()
