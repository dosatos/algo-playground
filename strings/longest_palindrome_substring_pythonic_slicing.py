class Solution:
    """
    https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.

    """
    def longestPalindrome(self, s: str) -> str:
        """SQUARED"""
        if s == s[::-1]:
            return s

        length = 1
        left_pointer = 1

        for i in range(1, len(s)):  # linear
            odd_left_pointer = i - length - 1
            even_left_pointer = i - length
            upto = i + 1

            odd_word = s[odd_left_pointer:upto]
            even_word = s[even_left_pointer:upto]

            if odd_left_pointer >= 0 and odd_word == odd_word[::-1]:  # linear
                print(odd_word)
                left_pointer = odd_left_pointer
                length += 2
            elif even_left_pointer >= 0 and even_word == even_word[::-1]:  # linear
                print(even_word)
                left_pointer = even_left_pointer
                length += 1

        return s[left_pointer:left_pointer + length]


def main():
    # text = "miycvxmqggnmmcwlmizfojwrurwhwygwfykyefxbgveixykdebenzitqnciigfjgrzzbtgeazyrbiirmejhdwcgjzwqolrturjlqpsgunuqerqjevbheblmbvgxyedxshswsokbhzapfuojgyfhctlaifrisgzqlczageirnukgnmnbwogknyyuynwsuwbumdmoqwxprykmazghcpmkdcjduepjmjdxrhvixxbfvhybjdpvwjbarmbqypsylgtzyuiqkexgvirzylydrhrmuwpmfkvqllqvekyojoacvyrzjevaupypfrdguhukzuqojolvycgpjaendfetkgtojepelhcltorueawwjpltehbbjrvznxhahtuaeuairvuklctuhcyzomwrrznrcqmovanxmiyilefybkbveesrxkmqrqkowyrimuejqtikcjfhizsmumajbqglxrvevexnleflocxoqgoyrzgqflwiknntdcykuvdcpzlakljidclhkllftxpinpvbngtexngdtntunzgahuvfnqjedcafzouopiixw"
    text = "xxracecarracecarxxz"
    s = Solution()
    print(s.longestPalindrome(text))


if __name__ == '__main__':
    main()