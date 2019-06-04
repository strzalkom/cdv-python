def potega(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    else:
        return podstawa * potega(podstawa, wykladnik - 1)


print(potega(3, 3))

'''
    potega(3, 3) --> 27 --> 3 * 9
    potega(3, 2) --> 9 --> 3 * 3
    potega(3, 1) --> 3 --> 3 * 1
    potega(3, 0) --> 1
'''
