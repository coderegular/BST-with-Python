import random
import math


# Constant Variables
LEN_OF_LIST = 20
BEGIN = 1
END = 20
NUM = 2


def make_data():
    my_data = []
    for i in range(LEN_OF_LIST):
        my_data.append(random.randint(BEGIN, END))
    return my_data


def bst(my_data, number):
    middle = math.floor(len(my_data)/2)
    if len(my_data) > 1:
        if my_data[middle] == number:
            return True
        elif number <= my_data[middle]:
            return bst(my_data[0:middle], number)
        elif number > my_data[middle]:
            return bst(my_data[middle:], number)
    else:
        return True if number == my_data[middle] else False


def main():
    data = make_data()
    data.sort()
    print(f"The crated list items is:\n{data}")
    print(f"The number you are searching is: {NUM}")
    if bst(data, NUM):
        print(f"we found the specified number: {NUM}.")
    else:
        print(f"The specified number does not exists.")


if __name__ == '__main__':
    main()
