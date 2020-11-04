from fuzzywuzzy import (
    fuzz,
    process)


def ratio_test(word_a, word_b):
    # test 1
    print("Simple Ratio: ",
          fuzz.ratio(word_a, word_b))
    # test 2
    print("Partial Ratio: ",
          fuzz.partial_ratio(word_a, word_b))
    # test 3
    print("Token Sort Ratio: ",
          fuzz.token_sort_ratio(word_a, word_b))
    # test 4
    print("Token Set Ratio: ",
          fuzz.token_sort_ratio(word_a, word_b))


def process_test():
    pass


if __name__ == '__main__':
    ratio_test(word_a="I Love You I", word_b="You Lobe I I")