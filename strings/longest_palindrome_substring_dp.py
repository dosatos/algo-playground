cache = {}


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = None
        max_step = len(s)
        for step in range(0, max_step + 1):
            for left in range(0, len(s) - step):
                right = left + step
                if self._is_palindrome(s, left, right):
                    result = s[left:right + 1]
        return result

    def _is_palindrome(self, s: str, left: int, right: int):
        if (left, right) in cache:
            return cache[(left, right)]
        if s[left] == s[right]:
            if right - left == 0 or right - left == 1:
                cache[(left, right)] = True
                return True
            result = self._is_palindrome(s, left + 1, right - 1)
            cache[(left, right)] = result
            return result
        cache[(left, right)] = False
        return False


def main():
    text = "miycvxmqggnmmcwlmizfojwrurwhwygwfykyefxbgveixykdebenzitqnciigfjgrzzbtgeazyrbiirmejhdwcgjzwqolrturjlqpsgunuqerqjevbheblmbvgxyedxshswsokbhzapfuojgyfhctlaifrisgzqlczageirnukgnmnbwogknyyuynwsuwbumdmoqwxprykmazghcpmkdcjduepjmjdxrhvixxbfvhybjdpvwjbarmbqypsylgtzyuiqkexgvirzylydrhrmuwpmfkvqllqvekyojoacvyrzjevaupypfrdguhukzuqojolvycgpjaendfetkgtojepelhcltorueawwjpltehbbjrvznxhahtuaeuairvuklctuhcyzomwrrznrcqmovanxmiyilefybkbveesrxkmqrqkowyrimuejqtikcjfhizsmumajbqglxrvevexnleflocxoqgoyrzgqflwiknntdcykuvdcpzlakljidclhkllftxpinpvbngtexngdtntunzgahuvfnqjedcafzouopiixw"
    s = Solution()
    print(s.longestPalindrome(text))


if __name__ == '__main__':
    main()