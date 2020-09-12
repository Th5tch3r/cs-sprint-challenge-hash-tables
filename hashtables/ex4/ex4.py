def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {n: False for n in a}
    result = []
    for n in a:
        if n != 0 and -n in ht and not ht[n] and not ht[-n]:
            ht[-n] = True
            ht[n] = True
            result.append(abs(n))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
