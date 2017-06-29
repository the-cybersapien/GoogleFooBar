import itertools
from fractions import gcd


def answer(banana_list):
    def check_forever(x, y):
        if y > x:
            x, y = y, x

        z = (x + y) / gcd(x, y)
        return bool((z - 1) & z)

    b_list = set()
    combinations = list(itertools.combinations(banana_list, 2))
    for com in combinations:
        if check_forever(com[0], com[1]):
            b_list.add(com[0])
            b_list.add(com[1])

    return len(banana_list) - len(b_list)


print answer([1, 7, 3, 21, 13, 19])
