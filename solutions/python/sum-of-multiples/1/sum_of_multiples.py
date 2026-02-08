def sum_of_multiples(limit, multiples):
    multiple = []
    for i in range(limit):
        for j in multiples:
            if j == 0:
                continue
            elif i % j == 0:
                multiple.append(i)
    return sum(set(multiple))