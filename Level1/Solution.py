
    def answer(s):
        # your code here
        maxOcc = 0
        mySet = set()
        for x in xrange(0, len(s)):
            for y in xrange(x + 1, len(s) + 1):
                str = s[x:y]
                if str not in mySet:
                    occ = s.count(str)
                    if occ > maxOcc and len(s.replace(str, '')) is 0:
                        maxOcc = occ
                    mySet.add(str)

        return maxOcc