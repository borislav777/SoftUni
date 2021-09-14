def numbers_searching(*args):
    result = []
    dub = []
    for num in range(min(args), max(args) + 1):

        if num not in args:
            result.append(num)
        if args.count(num) > 1:
            dub.append(num)
    result.append(dub)
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))