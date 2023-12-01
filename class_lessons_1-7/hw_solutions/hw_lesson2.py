import unittest


def occurrence_counter(input1, input2, case_sensative=True):
    input1 = str(input1)
    input2 = str(input2)
    if not case_sensative:
        input1 = input1.lower()
        input2 = input2.lower()
    return input1.count(input2)


class OccurrenceCounterTest(unittest.TestCase):
    def test_basic_single_count(self):
        self.assertEqual(1, occurrence_counter("Cucumber", "c"))

    def test_basic_multi_count(self):
        self.assertEqual(2, occurrence_counter("Cucumber", "u"))

    def test_basic_zero_count(self):
        self.assertEqual(0, occurrence_counter("Cucumber", "x"))

    def test_adv_upper_count(self):
        self.assertEqual(2, occurrence_counter("Cucumber", "U", False))

    def test_adv_lower_count(self):
        self.assertEqual(2, occurrence_counter("Cucumber", "c", False))

    def test_adv_multi_char_count(self):
        self.assertEqual(1, occurrence_counter("Cucumber", "Uc", False))

    def test_exp_str_int_count(self):
        self.assertEqual(1, occurrence_counter("The boy was 5 years old", 5))

    def test_exp_int_count(self):
        self.assertEqual(3, occurrence_counter(60224012, 2))

    def test_exp_int_str_count(self):
        self.assertEqual(1, occurrence_counter(60224012, "12"))


if __name__ == '__main__':
    unittest.main()
