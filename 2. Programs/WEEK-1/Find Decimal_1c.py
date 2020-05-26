def decimalCount(number):

    if len(number) == number.count('9'):

        return len(number)+1

    else:
        return len(number)




if __name__ == "__main__":

    n = input()

    decCount = decimalCount(n)

    print(decCount)
