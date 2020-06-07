# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5,
# 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

def sumMultiples(a):
    total = 0
    for i in range(a):
        if(((i%3==0) & (i%5==0)) | (i%3==0) | (i%5==0)):
            total+=i
        else:
            pass

    return total


def main():
    num = 1000
    print(sumMultiples(num))


if __name__ == "__main__":
    main()
