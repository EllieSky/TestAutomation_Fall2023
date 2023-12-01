import unittest


def calculate_sum(num1, num2, num3=0):
    if type(num1) == int or type(num1) == float:
        if type(num2) == int or type(num2) == float:
            result = num1 + num2 + num3
            return result
    raise TypeError("Parameters for this function must be numeric")



class MyFirstUnitTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        self.assertEqual(False, False)  # add assertion here
        self.assertNotEqual(True, False)  # add assertion here

    def test_add_positive_ints(self):
        actual_result = calculate_sum(2, 3)
        self.assertEqual(5, actual_result)

    def test_add_positive_and_negative_ints(self):
        actual_result = calculate_sum(-10, 10)
        self.assertEqual(0, actual_result)

    def test_add_decimals(self):
        actual_result = calculate_sum(1.5, 3.25)
        self.assertEqual(4.75, actual_result)

    def test_add_words_raises_type_error(self):
        # actual_result = calculate_sum('hello', 'class')
        self.assertRaises(TypeError, calculate_sum, 'hello', 'class')

    def test_add_three_positive_ints(self):
        actual_result = calculate_sum(2, 3, 50)
        self.assertEqual(55, actual_result)

if __name__ == '__main__':
    unittest.main()
