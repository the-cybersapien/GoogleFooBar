import itertools


def answer(num_buns, num_required):
    ansList = []
    if num_buns == num_required:
        for x in xrange(num_buns):
            ansList.append([x])
    elif num_required == 1:
        for x in xrange(num_buns):
            ansList.append([0])
    else:
        # Use Pigeonhole Principle, this thing is a mess
        basicCombinations = itertools.combinations(xrange(num_buns), num_required)
        totals = len(list(basicCombinations)) * num_required
        repeatTime = num_buns - num_required + 1
        newcombinations = list(itertools.combinations(xrange(num_buns), repeatTime))
        # Make empty 1-D array
        for x in range(num_buns):
            ansList.append([])
        # Actually put values in the array
        for x in range(totals / repeatTime):
            for y in newcombinations[x]:
                ansList[y].append(x)

    return ansList


if __name__ == '__main__':
    print answer(5, 3)
