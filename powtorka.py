# staz pierwszy miesiac za darmo potem platne
x = int


def this_fails():
    x = 1/0
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)


this_fails()
