def gen(total):
    i = 0
    sum = 0
    count = 0
    while sum + (i * 2) <= total:
        if i == 0:
            i = 1
        else:
            i *= 2
        sum += i
        count += 1
    if (total - sum) >= (i + (i / 2)):
        return count + 1
    return count


def sting(total):
    sum = 1
    count = 1
    m = 0
    n = 1
    while sum + n < total and sum + m + n <= total:
        k = m + n
        sum += k
        count += 1
        m = n
        n = k
    return count


def answer(total_lambs):
    if total_lambs < 10 or total_lambs > 1000000000:
        return 0
    return sting(total_lambs) - gen(total_lambs)
