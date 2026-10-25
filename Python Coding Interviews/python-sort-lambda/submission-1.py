from typing import List


def sort_words(words: List[str]) -> List[str]:
    sorted_list = sorted(words , key = lambda x : len(x) , reverse = True)
    return sorted_list


def sort_numbers(numbers: List[int]) -> List[int]:
    sorted_list = sorted(numbers , key = lambda x : abs(x) , reverse = False)
    return sorted_list


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
