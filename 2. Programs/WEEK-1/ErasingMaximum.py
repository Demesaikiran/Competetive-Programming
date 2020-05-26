# THIS IS THE FUNCTION WHICH REMOVES THE MAXIMUM ELEMENT IN THE LIST

def EraseMaximum(a):

    maxy = max(a)
    maxCount = a.count(maxy)
    count = 0

    if maxCount < 3:
        a.remove(maxy)
        return a
    else:

        for i in range(len(a)):
            if a[i] == maxy:
                count += 1

            if count == 3:
                del(a[i])
                return a

            else:
                continue


if __name__ == "__main__":

    # N IS LENGTH OF THE ARRAY
    n = int(input())

    inList = list(map(int, input().strip().split()))[:n]

    inList = EraseMaximum(inList)

    print(*inList)
    
