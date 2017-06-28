def answer(s):
    count = 0
    # Bitwise to the rescue!
    while len(s) > 0 and int(s) > 1:
        # Check if last bit is 0
        if int(s[-1:]) % 2 == 0:
            s = str(int(s) / 2)
        # Check if bit-mask is 01
        elif (len(s) == 1 and int(s[-1:])) or int(s[-2:]) % 4 == 1:
            s = str(int(s) - 1)
        # Check if bit-mask is 11
        else:
            s = str(int(s) + 1)
        count += 1
    return count

if __name__ == '__main__':
    print answer('52185')
