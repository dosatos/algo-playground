"""

Then numbers are integers
What's N? What's the largest value? Only positive, non-negative?
Is the array sorted?

test cases

We can only remove, right?

[]
[3, 2, 1] {3: 1, 2: 1, 1: 1}
[2, 2, 2]

       |
[1, 1, 1, 1] {3:2, 2:1, 1:1}
          |

sort
left on the beginning
right on the second largest
while left != right:
    decrease by the difference b/w current and second largest
    left += 1
    count += 1

When left == right, then move the right to the next second largest

Continue doing this until it is the smallest value (0? 1?) Assume it is 1

"""
from typing import List


def min_moves_to_equal(array: List[int]):
    array = sorted(array, reverse=True)
    count = 0
    for i in range(1, len(array)):
        count += i if array[i] != array[i-1] else 0
    return count


# def min_moves_to_equal(array: List[int]) -> int:
#     array = sorted(array, reverse=True)
#     result = 0
#     for i in range(1, len(array)):
#         result += i if array[i] != array[i - 1] else 0
#     return result
#
#
def _min_moves_to_equal(piles: List[int]) -> int:
    """
    Brute force: O(N^2)
    """
    count = 0
    piles = sorted(piles, reverse=True)  # O NLogN
    least = min(piles)
    left = right = 0
    while piles[left] != least:  # O N^2
        left = 0
        while piles[left] == piles[right]:
            right += 1
        while left != right:
            difference = piles[left] - piles[right]
            piles[left] -= difference
            left += 1
            count += 1
    return count


def main():
    piles = [5, 4, 4, 2]
    piles = [5, 2, 1]
    assert min_moves_to_equal(piles) == _min_moves_to_equal(piles)
    print(min_moves_to_equal(piles))


if __name__ == '__main__':
    main()
