import unittest


# "the weather is really nice"  ->  "nice really is weather the"
def reverse_sentence(sentence: str):
    if sentence[-1] == '!':
        return reverse_sentence(sentence[:-1]) + '!'

    reversed_list = list(reversed(sentence.split()))
    if sentence[0].isupper():
        reversed_list[0] = (reversed_list[0]).capitalize()

        if reversed_list[-1] != 'I':
            reversed_list[-1] = (reversed_list[-1]).lower()

    return ' '.join(reversed_list)


class TestFunctions(unittest.TestCase):
    def test_reverse_basic_short_sentence(self):
        self.assertEqual("nice really is weather the", reverse_sentence("the weather is really nice"))

    def test_reverse_capitalized_short_sentence(self):
        self.assertEqual("Nice really is weather the", reverse_sentence("The weather is really nice"))

    def test_reverse_multi_capitalized_short_sentence(self):
        self.assertEqual("Late minutes 2 was I but now here am I",
                         reverse_sentence("I am here now but I was 2 minutes late"))

    def test_reverse_short_sentence_with_punctuation(self):
        self.assertEqual("Nice really is weather the!", reverse_sentence("The weather is really nice!"))


if __name__ == '__main__':
    unittest.main()
