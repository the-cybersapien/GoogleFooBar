def answer(l):
    count = 0
    for y in xrange(1, len(l) - 1):
        xList = [x for x in l[:y] if l[y] % x == 0]
        xCount = len(xList)
        
        zList = [z for z in l[y + 1:] if z % l[y] == 0]
        zCount = len(zList)
        count += xCount * zCount
    return count
