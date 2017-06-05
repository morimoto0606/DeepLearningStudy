def AND(x1, x2):
    w1 = 0.5
    w2 = 0.5
    theta = 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

AND(0.1,1)
