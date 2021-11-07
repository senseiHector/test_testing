from unittest import TestCase, mock

from main import OurClass , our_magic_function


class TestMain(TestCase):
    # def test_our_function(self):
    #     # mock_our_class = mock.MagicMock()
    #     # mock_our_class.our_value = 'mock value'
    #     # self.assertEqual('mock value', our_function().our_value)
    #     pass
    #
    # @mock.patch('main.our_function')
    # def test_our_second_function(self, mock_our_function):
    #     mock_our_class = mock.MagicMock()
    #     mock_our_class.our_value = 'mock value'
    #     mock_our_function.return_value = mock_our_class
    #     self.assertEqual(our_second_function(), 'mock value')

    def test_our_addition(self):
        self.assertEqual(10, OurClass().our_addition(5))

    @mock.patch('main.OurClass.our_addition', return_value=10)
    def test_our_second_addition(self, mock_our_addition):
        self.assertEqual(20, OurClass().our_second_addition(5))
        mock_our_addition.assert_called_once()

    @mock.patch('main.OurClass.our_addition', return_value=10)
    def test_our_multiplication(self, mock_our_addition):
        self.assertEqual(30, OurClass().our_multiplication(3))
        self.assertEqual(3, mock_our_addition.call_count)

    @mock.patch('main.our_function')
    def test_our_magic_function(self, mock_our_function):
        mock_our_class = mock.MagicMock()
        mock_our_class.our_magic_value = 17
        mock_our_function.return_value = mock_our_class
        self.assertEqual(our_magic_function(2), mock_our_class.our_magic_value)


