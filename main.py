# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class OurClass:
    def __init__(self, magic=None):
        self.our_value = 5
        self.our_second_value = 10
        self.our_magic_value = magic + self.our_value + self.our_second_value

    def our_addition(self, number):
        return self.our_value + number

    def our_second_addition(self, number):
        return self.our_addition(number) + self.our_second_value

    def our_multiplication(self, number):
        our_sum = 0
        for i in range(number):
            our_sum += self.our_addition(number)
        return our_sum


def our_function(number):
    return OurClass(number)


def our_second_function():
    our_instance = our_function()
    return our_instance.our_value


def our_third_function():
    print('called')


def our_magic_function(number):
    our_instance = our_function(number)
    return our_instance.our_magic_value


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(our_function().our_value)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
