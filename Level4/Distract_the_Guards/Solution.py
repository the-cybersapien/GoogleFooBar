from fractions import gcd


def answer(banana_list):
    def check_forever(x, y):
        if y > x:
            x, y = y, x

        z = (x + y) / gcd(x, y)
        return bool((z - 1) & z)
    # Sort the list first
    banana_list.sort()
    # Create a second list to store those values which do not have any match
    lst = list()
    # Iterate through the original list, in such a way that once the element is accessed, it is removed.
    while len(banana_list) > 0:
    	noMatch = True
    	# Since we're removing the starting element anyway, always access the first element
    	x = banana_list[0]
    	for i in xrange(len(banana_list) - 1, -1, -1):
    		y = banana_list[i]
    		if check_forever(x, y):
    			banana_list.remove(x)
    			banana_list.remove(y)
    			noMatch = False
    			break
    	if noMatch:
    		lst.append(x)
    		banana_list.remove(x)
    return len(lst)


print answer([1, 7, 3, 21, 13, 19])
